import pandas as pd
import numpy as np

def CALC_NEW_MIXTURE(NP_VAF, DIMENSION, num_of_clusters, membership) :
    mixture = np.zeros((DIMENSION, num_of_clusters))

    for j in range(num_of_clusters) :
        num_of_this_cluster = len(membership[membership==j]) # 이 멤버십에 속하는 원소 개수

        for i in range(DIMENSION):
            membership_index_list = np.where(membership==j)[0]
            sum = 0
            mean_vaf = 0

            for n in membership_index_list :
                sum += NP_VAF[i][int(n)]

             # membership 별 mean vaf
            
            mean_vaf = float(sum / num_of_this_cluster)
            mixture[i][j] = round(mean_vaf, 5)

    return mixture
       

def RUNNING_MSTEP(NP_VAF, DIMENSION,num_of_clusters, membership) :
    mixture = CALC_NEW_MIXTURE(NP_VAF, DIMENSION,num_of_clusters, membership) 
    return mixture
