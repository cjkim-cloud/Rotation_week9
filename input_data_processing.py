import pandas as pd 
import numpy as np


file_path = "input file path"
df = pd.read_csv(file_path, sep ="\t", header = None)


dimension = int( len(df.iloc[0, 2].split(",")) / 2 )
variant_number = len((df))

np_vaf = np.zeros((dimension, variant_number))
depth_list = np.zeros((dimension, variant_number))
alt_list = np.zeros((dimension, variant_number))
np_BQ = np.zeros((dimension, variant_number))


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
            np_vaf[sample_index][row] = 0
        else :
            np_vaf[sample_index][row] = round(float(alt) / float(depth), 2)


df_alt = pd.DataFrame(alt_list)
df_depth = pd.DataFrame(depth_list)

'''
df_alt.to_csv(file_path + "0.input_df_alt.txt", sep="\t", index=False, header=False)
df_depth.to_csv(file_path + "0.input_df_depth.txt", sep="\t", index=False, header=False)

pd.DataFrame(np_vaf).to_csv(file_path + "0.input_npvaf.txt", sep ="\t", index = False, header=False)
pd.DataFrame(np_BQ).to_csv(file_path + "0.input_npBQ.txt", sep ="\t", index = False, header=False)
'''
