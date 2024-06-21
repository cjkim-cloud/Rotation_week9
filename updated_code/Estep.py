import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import math

def CALC_POSTERIOL_THETA(NUM_OF_VARIANTS, DF_ALT, DF_DEPTH, DIMENSION, num_of_clusters, mixture) :

    #prior = 1 / float(num_of_clusters)
    theta = np.zeros((num_of_clusters, NUM_OF_VARIANTS))

    # posterior j * k 만큼 나옴 -> theta 에 저장

    for j in range(num_of_clusters):
        
        for k in range(NUM_OF_VARIANTS):
            posterior = 0
            for i in range(DIMENSION):
                alt_obs = int(DF_ALT.iloc[i][k]) # 해당 variant 의 시행 횟수 Nalt

                n_dist = int( DF_DEPTH.iloc[i][k] * mixture[i][j] * 2)
                        
                likelihood = scipy.stats.binom.pmf(alt_obs, n_dist, 0.5)
                if likelihood == 0 :
                    posterior += -400
                else :
                    posterior += math.log10(likelihood)
            
            theta[j][k] = posterior
    return theta


def CALC_DISTANCE_THETA(NP_VAF, NUM_OF_VARIANTS, DIMENSION, centroid, num_of_clusters) :
    distance_theta = np.zeros((num_of_clusters, NUM_OF_VARIANTS))
    for k in range(NUM_OF_VARIANTS) :
        for j in range(num_of_clusters) : 
            distance_sum = 0      
            for i in range(DIMENSION) :
                distance_sum += (centroid[i][j] - NP_VAF[i][k]) ** 2

            distance = np.sqrt(distance_sum)
            distance_theta[j][k] = round(distance, 5)

    return distance_theta

def ASSIGN_MEMBERSHIP(NUM_OF_VARIANTS, num_of_clusters, theta):
    membership = np.zeros((NUM_OF_VARIANTS), dtype=int) # [k]
    
    for k in range(NUM_OF_VARIANTS) :
        theta_per_cluster_list = []
        for j in range(num_of_clusters) :
            theta_per_cluster_list.append(theta[j][k]) # min list 에는 j 센트로이드 순서로 0번 - k 변이 |  1번 - k변이 | 2번 - k 변이 거리가 저장 

        max_cluster = theta_per_cluster_list.index(np.max(theta_per_cluster_list))
        membership[k] = int(max_cluster)
    
    return membership

def CALC_DISTANCE_INERTIA(NUM_OF_VARIANTS, membership, num_of_clusters, distance_theta) :
   
    distance_inertia = 0.0
    for k in range(NUM_OF_VARIANTS):

        assigned_cluster = int(membership[k]) # k 번째 변이의 클러스터 번호는 membership[k] 로 접근할 수 있음.
        i = distance_theta[assigned_cluster][k] # k변이와 그의 cluster 거리는 [assigned 클러스터][변이번호] 로 접근할 수 있음. 이를 제곱해서 더해주면 됨. 

        distance_inertia += float(i ** 2) 

    return distance_inertia


def RUNNING_ESTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, mixture, DF_ALT, DF_DEPTH) :

    theta = CALC_POSTERIOL_THETA(NUM_OF_VARIANTS, DF_ALT, DF_DEPTH, DIMENSION, num_of_clusters, mixture)
    membership = ASSIGN_MEMBERSHIP( NUM_OF_VARIANTS, num_of_clusters, theta)
    distance_theta = CALC_DISTANCE_THETA(NP_VAF, NUM_OF_VARIANTS, DIMENSION, mixture, num_of_clusters)
    distance_inertia = CALC_DISTANCE_INERTIA(NUM_OF_VARIANTS,  membership,  num_of_clusters, distance_theta)


    return theta, membership, distance_inertia

