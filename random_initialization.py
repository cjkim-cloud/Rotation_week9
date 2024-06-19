def RANDOM_CHOOSE_INT(NUM_OF_VARIANTS, size=5) :
    first_index_list = np.random.choice(NUM_OF_VARIANTS, size=size, replace=False)
    
    return first_index_list

def CENTROID_KMEANS_PLUS_PLUS(NP_VAF, NUM_OF_CLUSTERS, NUM_OF_VARIANTS, DIMENSION, first_index):
    centroid_list = np.zeros((DIMENSION, NUM_OF_CLUSTERS))  # Initialize centroid list
    
    # Step 1: Randomly select the first centroid from NP_VAF
    first_index = first_index
    for i in range(DIMENSION):
        centroid_list[i][0] = NP_VAF[i][first_index]
    
    #ok 
    
    # Step 2: Select subsequent centroids using K-Means++ method
    for t in range(1, NUM_OF_CLUSTERS): # 1,2 즉 j-1 개의 centroid 를 추가 (첫번째에서 하나 정해줬으니 나머지 j-1)
        sum_sq_distances = np.zeros(NUM_OF_VARIANTS)
        
        # Calculate squared distances to the nearest centroid for each data point
        for k in range(NUM_OF_VARIANTS):
            min_sq_distance = np.inf # 매우 큰 값 양의 무한대를 초기값으로.
            for j in range(t):
                sq_distance = np.sum((centroid_list[: , j] - NP_VAF[: , k]) ** 2) # centroid 
                if sq_distance < min_sq_distance:
                    min_sq_distance = sq_distance
            sum_sq_distances[k] = min_sq_distance
            # 제일 가까운 기존 센트로이드와의 거리를 저장
        
        #이를 다음 센트로이드로 뽑힐 확률로 사용
        probabilities = sum_sq_distances / np.sum(sum_sq_distances)
        next_index = np.random.choice(NUM_OF_VARIANTS, p=probabilities)
        
        # 센트로이드 선택
        for i in range(DIMENSION):
            centroid_list[i][t] = NP_VAF[i][next_index]
    
    # 한번에 루트
    #distances_to_first = np.sqrt(np.sum((centroid_list[:, 0].reshape(-1, 1) - NP_VAF) ** 2, axis=0))
    
    return centroid_list
