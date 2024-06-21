import scores.py

def GET_TRIAL(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, last_step_list) :
    #제일 best 무슨 값을 가지는 애를 Trial 로 할까..

    gap_list = []
    for step in last_step_list :
        
        # 조건 만족 못한다 햇으면 false 를 넘겨줌 다음 스텝
        
        # vaf 합 0.5 이랑 차이 1퍼센트 이상 날때 (조건 못 맞췄을 때) 
        if not CHECK_VAF_SUM(step, DIMENSION):
            # - 100 패널티 # 조정해야함 그냥 패널티 준 거
            gap = CALC_GAP_SCORE(NP_VAF, NUM_OF_VARIANTS, DIMENSION, step.get_membership(), step.get_mixture(), num_of_clusters) - 100
        
        #vaf 합 0.5 일때
        else : 
            gap = CALC_GAP_SCORE(NP_VAF, NUM_OF_VARIANTS, DIMENSION, step.get_membership(), step.get_mixture(), num_of_clusters)

        gap_list.append(gap)

        max_index = np.argmax(gap_list)
        best_step = last_step_list[max_index]

        silhouette_score_alldata = silhouette_samples(NP_VAF.T , best_step.get_membership())
        silhouette_score = round(np.mean (silhouette_score_alldata), 5)
        
        
        best_step.set_silhouette_score(silhouette_score)
        best_step.set_gap_score(gap_list[max_index])

        trial = best_step.copy_to_trial_obj()
    return trial

def FIND_THE_BEST_K(cluster_hard_obj) :
    gap_list = []

    for trial in cluster_hard_obj :
        gap_list.append(trial.get_gap_score())

    max_index = np.argmax(gap_list)
    best_trial = cluster_hard_obj[max_index]

    return best_trial

