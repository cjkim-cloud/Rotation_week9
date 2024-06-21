import KMeans.py, Estep.py, Mstep.py, Record_obj.py, PROCESS_INPUT_DATA.py

def RUNNING_EMSTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, NUM_OF_EM_ITERATION, DF_ALT, DF_DEPTH) :
    #initial
    initial_membership, initial_mixture = PERFORM_KMEANS(NP_VAF, num_of_clusters, max_iteration=10)

    #initial_mixture = np.array(([[0.174, 0.02474, 0.30214], [0.30483, 0.0253, 0.20167]]))

    step_list =[]
    step_index = 0

    while step_index < NUM_OF_EM_ITERATION :
        theta, membership, distance_inertia = RUNNING_ESTEP(NP_VAF, NUM_OF_VARIANTS, DIMENSION, num_of_clusters, initial_mixture, DF_ALT, DF_DEPTH)
        mixture = RUNNING_MSTEP(NP_VAF, DIMENSION, num_of_clusters, membership)

        step_index += 1

        present_step = Step(membership, theta, mixture, distance_inertia, step_index, num_of_clusters)
        step_list.append(present_step)

        if step_index > 5 :
            previous_step = step_list[step_index - 1]
                #while break condition
            condition_1 =  np.abs(np.max(previous_step.get_theta()) - np.max(present_step.get_theta())) <= 0.01 * np.maximum(np.max(previous_step.get_theta()) , np.max(present_step.get_theta()))

            ## 0.01 이하로 이전 mixture 와 차이나기
            condition_2 = False not in (np.abs(previous_step.get_mixture() - present_step.get_mixture()) <= 0.01 * np.maximum(np.abs(previous_step.get_mixture()), np.abs(present_step.get_mixture())))

            # 이전 멤버십과 동일
            condition_3 = previous_step.get_membership() == present_step.get_membership()

            if condition_1 or condition_2 or condition_3 :
                break

    return step_list
