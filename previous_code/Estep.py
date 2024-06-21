
def CALC_DISTANCE_THETA(NP_VAF, NUM_OF_VARIANTS, DIMENSION, centroid, num_of_clusters) :
    theta = np.zeros((num_of_clusters, NUM_OF_VARIANTS))
    for k in range(NUM_OF_VARIANTS) :
        for j in range(num_of_clusters) : 
            distance_sum = 0      
            for i in range(DIMENSION) :
                distance_sum += (centroid[i][j] - NP_VAF[i][k]) ** 2

            distance = np.sqrt(distance_sum)
            theta[j][k] = round(distance, 5)

    return theta

def ASSIGN_MEMBERSHIP(NUM_OF_VARIANTS, num_of_clusters, theta):
    membership = np.zeros((NUM_OF_VARIANTS), dtype=int) # [k]
    
    for k in range(NUM_OF_VARIANTS) :
        min_list = []
        for j in range(num_of_clusters) :
            min_list.append(theta[j][k]) # min list 에는 j 센트로이드 순서로 0번 - k 변이 |  1번 - k변이 | 2번 - k 변이 거리가 저장 

        min_cluster = min_list.index(np.min(min_list))
        membership[k] = int(min_cluster)
    
    return membership

def CALC_INERTIA(NUM_OF_VARIANTS, membership, num_of_clusters, theta) :
   
    inertia = 0.0
    for k in range(NUM_OF_VARIANTS):

        assigned_cluster = int(membership[k]) # k 번째 변이의 클러스터 번호는 membership[k] 로 접근할 수 있음.
        i = theta[assigned_cluster][k] # k변이와 그의 cluster 거리는 [assigned 클러스터][변이번호] 로 접근할 수 있음. 이를 제곱해서 더해주면 됨. 

        inertia += float(i ** 2) 

    return inertia


def RUNNING_ESTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, centroid, num_of_clusters) :
    theta = CALC_DISTANCE_THETA(NP_VAF, NUM_OF_VARIANTS,  DIMENSION,centroid, num_of_clusters)
    membership = ASSIGN_MEMBERSHIP( NUM_OF_VARIANTS, num_of_clusters, theta)
    inertia = CALC_INERTIA(NUM_OF_VARIANTS,  membership,  num_of_clusters, theta)

    return theta, inertia, membership


    
