from sklearn.decomposition import PCA, TruncatedSVD
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib
import numpy as np
import pandas as pd
from scipy import stats

import improved_visualization.py
import input_data_processing.py
### calc_mean_mode 를 사용하기 위함인데 조정이 필요함 함수가 어려곳에 흩어져있음.


pca = PCA(n_components=2)
principalComponents = pca.fit_transform(np_vaf_3d.T)
np_pca = principalComponents
np_pca_T = np_pca.T # (sample index, variant index) 맞춰주기 위해 T


tcsvd = TruncatedSVD(n_components=2)
tcsvd.fit(np_vaf_3d.T)
np_tcsvd = tcsvd.transform(np_vaf_3d.T)
np_tcsvd_T = np_tcsvd.T

fig, ax = plt.subplots(1, 2, figsize=(22, 10))

### ##### 1 pic
x_data = np_pca_T[0]
y_data = np_pca_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth_3d]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[0].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[0].set_xlabel("Principal component 1", fontsize=15)
ax[0].set_ylabel("Principal component 2", fontsize=15)
ax[0].set_title("Answer_set 3D to 2D PCA : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for k, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth_3d == k)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {k} : {num_of_this_cluster}'))

ax[0].legend(handles=legend_list, title='Cluster', fontsize=10)

mean_list_pca, mode_list_pca = calc_mean_and_mode(np_pca_T, np_truth_3d, 2, 3)

ax[0].scatter(x=mean_list_pca[0], y=mean_list_pca[1], marker=8, s=80, label="mean", color='#009c11')
for x, y in zip(mean_list_pca[0], mean_list_pca[1]) :
    ax[0].text(x=x-0.01, y=y-0.01, s=f"mean [{x}, {y}]", color='#009c11', fontsize=10)


### mode 추가
ax[0].scatter(x=mode_list_pca[0], y=mode_list_pca[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list_pca[0], mode_list_pca[1]) :
    ax[0].text(x=x+0.01, y=y+0.01, s=f"mode [{x}, {y}]", color='#0048ff', fontsize=10)

### ### 2 pic ###
x_data = np_tcsvd_T[0]
y_data = np_tcsvd_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth_3d]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[1].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[1].set_xlabel("SVD 1", fontsize=15)
ax[1].set_ylabel("SVD 2", fontsize=15)
ax[1].set_title("Answer_set 3D to 2D truncated SVD : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for k, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth_3d == k)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {k} : {num_of_this_cluster}'))

ax[1].legend(handles=legend_list, title='Cluster', fontsize=10)

mean_list_svd, mode_list_svd = calc_mean_and_mode(np_tcsvd_T, np_truth_3d, 2, 3)

ax[1].scatter(x=mean_list_svd[0], y=mean_list_svd[1], marker=8, s=80, label="mean", color='#009c11')
for x, y in zip(mean_list_svd[0], mean_list_svd[1]) :
    ax[1].text(x=x-0.01, y=y-0.01, s=f"mean [{x}, {y}]", color='#009c11', fontsize=10)



### mode 추가
ax[1].scatter(x=mode_list_svd[0], y=mode_list_svd[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list_svd[0], mode_list_svd[1]) :
    ax[1].text(x=x+0.01, y=y+0.01, s=f"mode [{x}, {y}]", color='#0048ff', fontsize=10)

### go to and see "pca_svd_visualization.png"
