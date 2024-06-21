import numpy as np
import pandas as pd
import math

import Record_obj.py

def CHECK_VAF_SUM(step, DIMENSION) :
    mixture = step.get_mixture()
    num_of_clusters = step.get_num_of_clusters()
    
    vaf_sum = 0
    for i in range(DIMENSION): 
        for j in range(num_of_clusters) :
            vaf_sum += np.sum(mixture[i][j])
    
    vaf_mean_sum = vaf_sum / DIMENSION

    # 0.5와 mean vaf 합의 차이가 5퍼센트 이하일 때 true    
    result =  abs (vaf_mean_sum - 0.5) <=  0.05
    #result = abs (vaf_mean_sum - 0.5) <=  0.05 * max(abs(vaf_mean_sum), 0.5)

    if result :
        print(f"<PASS> mean vaf 합 0.5 이다. | sum of mean vaf : {vaf_mean_sum:.5f}")

    else : 
        print(f"<FAIL> mean vaf 합 0.5 이 아니다. | sum of mean vaf : {vaf_mean_sum:.5f}")

    return result
