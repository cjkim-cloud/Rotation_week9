def CALC_NEW_CENTROID(NP_VAF, NUM_OF_VARIANTS, DIMENSION,  membership,  num_of_clusters) :
    
    mixture = np.zeros((DIMENSION, num_of_clusters)) # 2차원 (sample index, cluster index)
    sum_list_per_cluster = np.zeros((DIMENSION, num_of_clusters))
    count_list_per_cluster = np.zeros(num_of_clusters)  # 각 멤버십 별 소속 멤버 개수


    for j in range(num_of_clusters) :
        count_list_per_cluster[j] = np.sum(membership == j) 
        


    for k in range(NUM_OF_VARIANTS):
        assigned_cluster = int(membership[k])

        for i in range(DIMENSION) :
            sum_list_per_cluster[i][assigned_cluster] += NP_VAF[i][k]

    

    for j in range(num_of_clusters):
        for i in range(DIMENSION):
            if np.sum(membership == j) == 0 :
                mixture[i][j] = 0.0
                ######## random 으로 뽑기 코드 달아놓으면 좋을듯
            else : 
                mixture[i][j] = round((sum_list_per_cluster[i][j] / count_list_per_cluster[j]), 5)

    return mixture

def RUNNING_MSTEP(NP_VAF, NUM_OF_VARIANTS,  DIMENSION, membership, num_of_clusters) :
    mixture = CALC_NEW_CENTROID(NP_VAF, NUM_OF_VARIANTS, DIMENSION, membership,  num_of_clusters) 
    return mixture
