
import KMeans.py, Estep.py, Mstep.py, EMstep.py, Record_obj.py, PROCESS_INPUT_DATA.py, save.py, scores.py
import VISUALIZATION.py, dimension_reduction.py

def MAIN(INPUT_PATH, OUTPUT_DIR) :

    DF_ALT, DF_DEPTH, NP_VAF, NP_TRUTH,DIMENSION, NUM_OF_VARIANTS = PROCESS_INPUT_DATA(INPUT_PATH)
    cluster_hard = Cluster_hard()

    for NUM_CLONE in range(2, 8) :
        num_of_clusters = NUM_CLONE
        last_step_list = []
        
        for NUM_TRIAL in range(0, 5) :  
            NUM_OF_EM_ITERATION = 10
            step_list =  RUNNING_EMSTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, NUM_OF_EM_ITERATION, DF_ALT, DF_DEPTH)
            last_step = step_list[-1]

            last_step_list.append(last_step)


        trial = GET_TRIAL(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, last_step_list)
        print(f" K : {num_of_clusters} , gap : {trial.get_gap_score()}, silhouette : {trial.get_silhouette_score()}, inertia : {trial.get_distance_inertia()}")

        cluster_hard.append(trial)

    cluster_hard_obj = cluster_hard.return_cluster_hard()

    # optimal k
    OPTIMAL_K_VISUALIZATION(OUTPUT_DIR, DIMENSION, cluster_hard_obj)
    CLUSTER_VISUALIZATION(OUTPUT_DIR, NP_VAF, cluster_hard_obj, DIMENSION, NP_TRUTH)
    
    best_trial = FIND_THE_BEST_K(cluster_hard_obj)

    # result report
    SAVE_RESULT(best_trial, INPUT_PATH, OUTPUT_DIR)
