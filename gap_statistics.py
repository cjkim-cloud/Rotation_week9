def GENERATE_REFERENCE(NP_VAF) :
    #bounds = np.array([np.min(NP_VAF, axis=0), np.max(NP_VAF, axis=0)]).T
    #return np.random.uniform(bounds[:, 0], bounds[:, 1], NP_VAF.shape)
    min_vals = np.min(NP_VAF, axis=0)
    max_vals = np.max(NP_VAF, axis=0)
    
    references = np.random.uniform(min_vals, max_vals, size=(NP_VAF.shape))

    return references

def CALC_GAP_SCORE(last_step_list, ref_last_step_list) :

    gap_score_list = []

    for last_step, ref_step in zip(last_step_list, ref_last_step_list) :
        gap = np.mean(np.log(ref_step.get_inertia())) - np.log(last_step.get_inertia())
        gap_score_list.append(gap)

    return gap_score_list

