from sklearn.metrics import adjusted_rand_score
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy import stats

import Kmeans.py

def CALC_ARI_SCORE(predicted_lables, NP_TRUTH) :
    cluster_result = predicted_lables
    true_labels = NP_TRUTH
    ari_score = round(adjusted_rand_score(true_labels, cluster_result) , 3)

    return ari_score

def CALC_LIKELIHOOD(NP_VAF, NUM_OF_VARIANTS, DIMENSION,num_of_clusters, mixture, membership):
    
    likelihood_allsample = np.zeros(NUM_OF_VARIANTS)
    for k in range(NUM_OF_VARIANTS):
        for i in range(DIMENSION):

            cluster = membership[k]
            
            alt_obs = int(NP_VAF[i][k] * 100)
            alt_dist, depth_dist = int(mixture[i][cluster] * 100) , 100
            
            #alt_obs = int(DF_ALT.iloc[i][k]) # 해당 variant 의 시행 횟수 Nalt
            #n_dist = int( DF_DEPTH.iloc[i][k] *  mixture[i][cluster] * 2)

            likelihood = scipy.stats.binom.pmf(alt_obs, depth_dist, 0.5)
            
            if likelihood == 0 :
                log_likelihood = -400
            else :
                log_likelihood = math.log10(likelihood)

        likelihood_allsample[k] += log_likelihood  

        likelihood_all = np.sum(likelihood_allsample)

    return likelihood_all

      


def GENERATE_REFERENCE(NP_VAF) :
    min_vals = np.min(NP_VAF, axis=0)
    max_vals = np.max(NP_VAF, axis=0)
    
    ref_NP_VAF = np.random.uniform(min_vals, max_vals, size=(NP_VAF.shape))

    return ref_NP_VAF


def CALC_GAP_SCORE(NP_VAF, NUM_OF_VARIANTS, DIMENSION, membership, mixture, num_of_clusters) :
    
    ref_wk_list =[]
    for _ in range(10) :
        ref_NP_VAF = GENERATE_REFERENCE(NP_VAF)    
        ref_membership, ref_mixture = PERFORM_KMEANS(NP_VAF, num_of_clusters, max_iteration=20)
        ref_wk = CALC_LIKELIHOOD(ref_NP_VAF, NUM_OF_VARIANTS, DIMENSION,num_of_clusters, ref_mixture, ref_membership)
        ref_wk_list.append(ref_wk)

    
    wk = CALC_LIKELIHOOD(NP_VAF, NUM_OF_VARIANTS, DIMENSION,num_of_clusters, mixture,membership)   

    gap = wk - np.mean(ref_wk_list) 

    return round(gap, 5) 
