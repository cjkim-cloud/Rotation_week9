import numpy as np
import pandas as pd


def PROCESS_INPUT_DATA(file_path):
    
    print("return ; DF_ALT, DF_DEPTH, NP_VAF, NP_TRUTH,DIMENSION, NUM_OF_VARIANTS")
    df = pd.read_csv(file_path, sep ="\t", header = None)
    DIMENSION = int( len(df.iloc[0, 2].split(",")) / 2 )
    NUM_OF_VARIANTS = len((df))

    NP_TRUTH = np.array(df.iloc[:][1])
    NP_VAF = np.zeros((DIMENSION, NUM_OF_VARIANTS))
    depth_list = np.zeros((DIMENSION, NUM_OF_VARIANTS))
    alt_list = np.zeros((DIMENSION, NUM_OF_VARIANTS))
    np_BQ = np.zeros((DIMENSION, NUM_OF_VARIANTS))


    for row in range(len(df)) : 
        depth_alt = df.iloc[row][2].split(",")
        
        # 1차원이면 0 , 2차원이면 0, 2, 3차원이면 0, 2, 4
        for i in range(0, len(depth_alt), 2) : 

            #depth alt
            depth = depth_alt[i]
            alt = depth_alt[i+1]

            # 1차원이면 0 / 2차원이면 0, 1 / 3차원이면 0, 1, 2
            sample_index = i // 2
            depth_list[sample_index][row] = depth
            alt_list[sample_index][row] = alt
            
            #BQ
            np_BQ[sample_index][row] = str(df.iloc[row][3]).split(",")[sample_index]


            if depth == 0 :
                NP_VAF[sample_index][row] = 0
            else :
                NP_VAF[sample_index][row] = round(float(alt) / float(depth), 5)


    DF_ALT = pd.DataFrame(alt_list)
    DF_DEPTH = pd.DataFrame(depth_list)

    return DF_ALT, DF_DEPTH, NP_VAF, NP_TRUTH,DIMENSION, NUM_OF_VARIANTS
