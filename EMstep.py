def RUNNING_EMSTEP(NP_VAF,  NUM_OF_VARIANTS, DIMENSION, centroid, num_of_clusters, NP_TRUTH=None) :  

    NUM_OF_ITERATION = 20
    step_index = 0

    #initial start
    theta, inertia, membership = RUNNING_ESTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, centroid, num_of_clusters) 
    mixture =  RUNNING_MSTEP(NP_VAF, NUM_OF_VARIANTS,  DIMENSION, membership, num_of_clusters)
    
    if NP_TRUTH is None :
        ari_score = None
    else :
        ari_score = CALC_ARI_SCORE(membership, NP_TRUTH)

    step_list = []
    step_list.append(Step(membership, theta, mixture, inertia, step_index, num_of_clusters, ari_score))

    print(f"===Initial start === \n iteration : {step_index} \nK : {num_of_clusters} \ncentroid : {centroid}")

    while step_index < NUM_OF_ITERATION :
        theta, inertia, membership = RUNNING_ESTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, mixture, num_of_clusters) 
        mixture =  RUNNING_MSTEP(NP_VAF, NUM_OF_VARIANTS,  DIMENSION, membership, num_of_clusters)
        
        if NP_TRUTH is None :
            ari_score = None
        else :
            ari_score = CALC_ARI_SCORE(membership, NP_TRUTH)

        step_index += 1
        
        step_tmp = Step(membership, theta, mixture, inertia, step_index, num_of_clusters , ari_score  )
        previous_mixture = step_list[step_index -1].get_mixture()

        ## 더이상 Centroid 에 이동이 없으면 early stopping
            # equal 보다는 몇 퍼센트 일치로 해볼 것.
            
        if step_index > 5 and np.array_equal(step_tmp.get_mixture(), previous_mixture) :
            print(f"******************************")
            print("THERE IS NO UPDATE")
            print(f"early stopping at iteration = {step_index}")
            print(f"******************************")
        
            break
        else :
            step_list.append(step_tmp)
            print(f"-- iteration : {step_index}, centroid {mixture}")

    print("계산은 끝\n")    

    return step_list

def GET_LAST_EMSTEP(NP_VAF,  NUM_OF_VARIANTS, DIMENSION, initial_centroid, num_of_clusters, NP_TRUTH=None) : 
   
    step_list = RUNNING_EMSTEP(NP_VAF,  NUM_OF_VARIANTS, DIMENSION, initial_centroid, num_of_clusters, NP_TRUTH)
    last_step = step_list[-1]

    return last_step




def RUNNING_ALL_EMSTEP(NP_VAF,  NUM_OF_VARIANTS, DIMENSION, NP_TRUTH=None) :
    
    ref_data = GENERATE_REFERENCE(NP_VAF)
    cluster_hard = Cluster_hard()
    ref_inertia_list= []

    for NUM_CLONE in range(2, 8) :

        num_of_clusters = NUM_CLONE # 2~7까지 바뀌는 cluster 수
        # 5개의 다른 시작 값 인덱스 생성
        first_index_list = RANDOM_CHOOSE_INT(NUM_OF_VARIANTS, size = 5)
        last_step_list = []

        ref_last_step_list = []        
    
        for NUM_TRIAL in range(0, 5) :   

            #initial 생성
            initial_centroid = CENTROID_KMEANS_PLUS_PLUS(NP_VAF, num_of_clusters, NUM_OF_VARIANTS, DIMENSION, first_index_list[NUM_TRIAL])
            ref_initial_centroid =  CENTROID_KMEANS_PLUS_PLUS(ref_data, num_of_clusters, NUM_OF_VARIANTS, DIMENSION, first_index_list[NUM_TRIAL])

            # 각 steps 마다 맨 마지막 최적 step 을 취함
            last_step = GET_LAST_EMSTEP(NP_VAF,  NUM_OF_VARIANTS, DIMENSION, initial_centroid, num_of_clusters, NP_TRUTH) 
            last_step_list.append(last_step)

            ref_last_step = GET_LAST_EMSTEP(ref_data,  NUM_OF_VARIANTS, DIMENSION, ref_initial_centroid, num_of_clusters) 
            ref_last_step_list.append(ref_last_step)
        
        # 가장 best ARI score 를 가지는 initial centroid step 을 trial 에 저장하는 과정 
        #best_index = FIND_THE_BEST_ARI_INDEX(last_step_list)
        # 
        gap_score_list = CALC_GAP_SCORE(last_step_list, ref_last_step_list)

        #elbow_score_list = CALC_ELBOW_SCORE()
        #silhouette_score_list = CALC_SILHOUETTE_SCORE()
         #best_index, best_gap_score, best_elbow_score, best_silhouette_score  = FIND_THE_BEST_STEP(last_step_list, gap_score_list, elbow_score_list, silhouette_score_list)


        #best_index = FIND_THE_BEST_ARI_INDEX(last_step_list)
        best_index = gap_score_list.index(np.max(gap_score_list))
        best_gap_score = gap_score_list[best_index]
        trial = last_step_list[best_index].copy_to_trial_obj() # step 에 정의된 함수로 객체 복사 저장

        trial.set_gap_score(best_gap_score)
        #trial.set_elbow_score(best_elbow_score)
        #trial.set_silhouette_score(best_silhouette_score)

        cluster_hard.append(trial)
        ref_inertia_list.append(ref_last_step_list[best_index].get_inertia())


    ## for 문 빠져나옴 ##
    # elbow 그림 그리기
    inertia_list =[]
    silhouette_list = []
    gap_score_list_v = []

    for trial in cluster_hard.return_cluster_hard() :
        silhouette_score_alldata = silhouette_samples(NP_VAF.T , trial.get_membership())
        silhouette_score = round(np.mean (silhouette_score_alldata), 5)
        gap_score = trial.get_gap_score()
        gap_score_list_v.append(gap_score)

        print(f" K : {trial.get_num_of_clusters()} || BEST ARI : {trial.get_ari_score()} || inertia : {trial.get_inertia()} || silhouette : {silhouette_score} || gap : {gap_score}")
        inertia_list.append(trial.get_inertia())
        silhouette_list.append(silhouette_score)
    
    fig, ax = plt.subplots(2, 2 , figsize=(16, 12))
    ax[0][0].plot(range(2, 8), inertia_list, color="#67abeb", label="observed data")
    ax[0][0].plot(range(2, 8), ref_inertia_list, color="#d44252", label = "reference data") # ref
    ax[0][0].legend(title="Inertia from")

    ax[0][0].set_xlabel("K (number of clusters)")
    ax[0][0].set_ylabel("inertia")
    ax[0][0].set_title(f"Elbow method : {DIMENSION}D / 0.txt")

    ax[0][1].plot(range(2, 8), silhouette_list, color="#3aad6f")
    ax[0][1].set_xlabel("K (number of clusters)")
    ax[0][1].set_ylabel("mean silhouette score")
    ax[0][1].set_title(f"Silhouette method : {DIMENSION}D / 0.txt")

    ax[1][0].plot(range(2, 8), gap_score_list_v, color="#9880d7")
    ax[1][0].set_xlabel("K (number of clusters)")
    ax[1][0].set_ylabel("gap score")
    ax[1][0].set_title(f"gap statistic : {DIMENSION}D / 0.txt")
    

    return cluster_hard



