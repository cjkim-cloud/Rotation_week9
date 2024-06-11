from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import pandas as pd
from scipy import stats

import input_data_processing.py

num_of_cluster = 3 ### 실습에서는 k=3 이라고 하자

def calc_mean_and_mode(np_vaf, np_truth, dimension, num_of_cluster):
    print("input argu ; np_vcf, np_truth, dimension, num_of_cluster")
    mean_list = np.zeros((dimension, num_of_cluster))
    for k in range(num_of_cluster) :
        for d in range(dimension) :
            mean_list[d][k] = round(np.mean(np_vaf[d][np_truth==k]), 2)
        
    mode_list = np.zeros((dimension, num_of_cluster))
    for k in range(num_of_cluster) :
        for d in range(dimension) : 
            mode_list[d][k] = round(stats.mode(np_vaf[d][np_truth==k])[0], 2) # mode는 [0] 이 최빈값 [1]에는 count

    print("return ; mean_list, mode_list")
    return mean_list, mode_list
  
      ## mean_list structure
      ## mean_list ( sample index ; i , cluster index ; k) 
      ## mean_list[0][0] == 0번 샘플의 0번 클러스터 mean vaf
      ## mean_list[1][0] == 1번 샘플의 0번 클러스터 mean vaf 
      ## 아래 등장할 그래프의 0번 클러스터 mean vaf x축 y축 값은 (mean_list[0][0], mean_list[0][1])

# preparation for visualization

df_alt_3d, df_depth_3d, np_vaf_3d, np_truth_3d, dimension_3d =  input_data_processing("3D data PATH")
df_alt, df_depth, np_vaf, np_truth, dimension =  input_data_processing("2D data PATH")

mean_list, mode_list = calc_mean_and_mode(np_vaf, np_truth, dimension, num_of_cluster)
mean_list_3d, mode_list_3d = calc_mean_and_mode(np_vaf_3d, np_truth_3d, dimension_3d, num_of_cluster)


## visualization running

fig, ax = plt.subplots(1, 2, figsize=(22, 10))

############### First, 2 dimension data
x_data = np_vaf[0]
y_data = np_vaf[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth]
  # np_truth 의 값 배열과 같은 크기 & 위치별 색상을 가지는 map 생성


ax[0].scatter(x_data, y_data, marker = 'o', s=20, c=color_map)
ax[0].set_xlabel("vaf of sample1", fontsize=15)
ax[0].set_ylabel("vaf of sample2", fontsize=15)
ax[0].set_title("Answer_set 2D : 0.txt (n=500) (depth=125x)", fontsize=20)

legend_list =[]
cluster =[0, 1, 2]

for k, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth == k)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {k} : {num_of_this_cluster}'))

ax[0].legend(handles=legend_list, title='Cluster', fontsize=10)

### mean 추가
ax[0].scatter(x=mean_list[0], y=mean_list[1], marker=8, s=80, label="mean", color='#009c11')

for x, y in zip(mean_list[0], mean_list[1]) :
    ax[0].text(x=x+0.01, y=y+0.01, s=f"mean [{x}, {y}]", color='#009c11')


### mode 추가
ax[0].scatter(x=mode_list[0], y=mode_list[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list[0], mode_list[1]) :
    ax[0].text(x=x-0.01, y=y-0.01, s=f"mode [{x}, {y}]", color='#0048ff')


###############  Second, 3 dimension data


ax[1] = fig.add_subplot(122, projection='3d')
ax[1].scatter(xs, ys, zs, c=color_map_3d, marker='o', s=15)

ax[1].set_title("Answer_set 3D : 0.txt (n=500) (depth=125x)", fontsize=20)

cluster=[0, 1, 2]

legend_list_2 = []
for k, color in zip(cluster, color_3d) :
    num_of_this_cluster= np.sum(np_truth_3d == k)
    legend_list_2.append(mpatches.Patch(color=color, label=f'Cluster {k} : {num_of_this_cluster}'))

ax[1].scatter(mean_list_3d[0], mean_list_3d[1], mean_list_3d[2], marker=8, s=100, label="mean", color='#009c11')

for x, y, z in zip(mean_list_3d[0], mean_list_3d[1], mean_list_3d[2]) :
    ax[1].text(x=x+0.01, y=y+0.01, z= z+0.01,s=f"mean [{x}, {y}, {z}]", color='#009c11')


### mode 추가
ax[1].scatter(mode_list_3d[0], mode_list_3d[1], mode_list_3d[2], marker=9, s=80, label="mode", color='#0048ff')

for x, y, z in zip(mode_list_3d[0], mode_list_3d[1], mode_list_3d[2]) :
    ax[1].text(x=x-0.01, y=y-0.01, z=z-0.01, s=f"mode [{x}, {y}, {z}]", color='#0048ff')

ax[1].legend(handles=legend_list_2, title='Cluster', fontsize=8)

