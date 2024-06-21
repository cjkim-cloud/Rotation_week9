
fig, ax = plt.subplots(3, 2 , figsize=(30, 25))

### ##### 0, 0 pic
x_data = np_vaf[0]
y_data = np_vaf[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[0][0].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[0][0].set_xlabel("vaf of Sample 1", fontsize=15)
ax[0][0].set_ylabel("vaf of Sample 2", fontsize=15)
ax[0][0].set_title("Answer_set 2D : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth == j)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))

ax[0][0].legend(handles=legend_list, title='Cluster', fontsize=10)

mean_list, mode_list = calc_mean_and_mode(np_vaf, np_truth, 2, 3)

#means
ax[0][0].scatter(x=mean_list[0], y=mean_list[1], marker=8, s=80, label="mean", color='#009c11')
for x, y in zip(mean_list[0], mean_list[1]) :
    ax[0][0].text(x=x-0.01, y=y-0.01, s=f"mean [{x}, {y}]", color='#009c11', fontsize=10)

### mode 추가
ax[0][0].scatter(x=mode_list[0], y=mode_list[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list[0], mode_list[1]) :
    ax[0][0].text(x=x+0.01, y=y+0.01, s=f"mode [{x}, {y}]", color='#0048ff', fontsize=10)

############# pic 0,1


np_kmeans_label, kmeans_centroid_list = RUNNING_KMEANS(np_vaf, 3)
normal_ari = CALC_ARI_SCORE(predicted_lables=np_kmeans_label, np_truth=np_truth)

x_data = np_vaf[0]
y_data = np_vaf[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_kmeans_label]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[0][1].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[0][1].set_xlabel("vaf of Sample 1", fontsize=15)
ax[0][1].set_ylabel("vaf of Sample 2", fontsize=15)
ax[0][1].set_title("KMeans Clustering Set 2D  : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

ax[0][1].scatter(x=kmeans_centroid_list[0], y=kmeans_centroid_list[1], marker='P', s=80, label="centroid", color='blue')
for x, y in zip(kmeans_centroid_list[0], kmeans_centroid_list[1]) :
    ax[0][1].text(x=x-0.01, y=y-0.01, s=f"centroid [{x}, {y}]", color='blue', fontsize=10)

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_kmeans_label == k)
    legend_list.append(mpatches.Patch(color=color, label=f'KMeans Cluster {j} : {num_of_this_cluster}'))

ax[0][1].text(x= 0.05, y= 0.95 , s=f"ARI score : {normal_ari}",color = 'red' , fontsize = 15, transform=ax[0][1].transAxes, verticalalignment='top', horizontalalignment='left')


ax[0][1].legend(handles=legend_list, title='KMeans Cluster', fontsize=10)



### ##### 1,0 pic
x_data = np_pca_T[0]
y_data = np_pca_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth_3d]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[1][0].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[1][0].set_xlabel("Principal component 1", fontsize=15)
ax[1][0].set_ylabel("Principal component 2", fontsize=15)
ax[1][0].set_title("Answer_set 3D to 2D PCA : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth_3d == j)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))

ax[1][0].legend(handles=legend_list, title='Cluster', fontsize=10)

mean_list_pca, mode_list_pca = calc_mean_and_mode(np_pca_T, np_truth_3d, 2, 3)

ax[1][0].scatter(x=mean_list_pca[0], y=mean_list_pca[1], marker=8, s=80, label="mean", color='#009c11')
for x, y in zip(mean_list_pca[0], mean_list_pca[1]) :
    ax[1][0].text(x=x-0.01, y=y-0.01, s=f"mean [{x}, {y}]", color='#009c11', fontsize=10)


### mode 추가
ax[1][0].scatter(x=mode_list_pca[0], y=mode_list_pca[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list_pca[0], mode_list_pca[1]) :
    ax[1][0].text(x=x+0.01, y=y+0.01, s=f"mode [{x}, {y}]", color='#0048ff', fontsize=10)



### ##### 1,1 pic
np_kmeans_label_pca, kmeans_centroid_list_pca = RUNNING_KMEANS(np_pca_T, 3)

pca_ari = CALC_ARI_SCORE(predicted_lables=np_kmeans_label_pca, np_truth=np_truth_3d)


x_data = np_pca_T[0]
y_data = np_pca_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_kmeans_label_pca]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[1][1].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[1][1].set_xlabel("Principal component 1", fontsize=15)
ax[1][1].set_ylabel("Principal component 2", fontsize=15)
ax[1][1].set_title("KMeans Clusterung set 3D to 2D PCA : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_kmeans_label_pca == j)
    legend_list.append(mpatches.Patch(color=color, label=f'KMeans Cluster {j} : {num_of_this_cluster}'))

ax[1][1].text(x= 0.05, y= 0.95 , s=f"ARI score : {pca_ari}", color = 'red' , fontsize = 15, transform=ax[1][1].transAxes,  verticalalignment='top', horizontalalignment='left')

ax[1][1].legend(handles=legend_list, title='KMeans Cluster', fontsize=10)

ax[1][1].scatter(x=kmeans_centroid_list_pca[0], y=kmeans_centroid_list_pca[1],  marker='P', s=80, label="centroid", color='blue')
for x, y in zip(kmeans_centroid_list_pca[0], kmeans_centroid_list_pca[1]) :
    ax[1][1].text(x=x-0.01, y=y-0.01, s=f"Centroid [{x}, {y}]", color='blue', fontsize=10)



### ### 2, 0 pic ####################
x_data = np_tcsvd_T[0]
y_data = np_tcsvd_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_truth_3d]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[2][0].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[2][0].set_xlabel("SVD 1", fontsize=15)
ax[2][0].set_ylabel("SVD 2", fontsize=15)
ax[2][0].set_title("Answer_set 3D to 2D truncated SVD : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_truth_3d == j)
    legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))

ax[2][0].legend(handles=legend_list, title='Cluster', fontsize=10)

mean_list_svd, mode_list_svd = calc_mean_and_mode(np_tcsvd_T, np_truth_3d, 2, 3)

ax[2][0].scatter(x=mean_list_svd[0], y=mean_list_svd[1], marker=8, s=80, label="mean", color='#009c11')
for x, y in zip(mean_list_svd[0], mean_list_svd[1]) :
    ax[2][0].text(x=x-0.01, y=y-0.01, s=f"mean [{x}, {y}]", color='#009c11', fontsize=10)



### mode 추가
ax[2][0].scatter(x=mode_list_svd[0], y=mode_list_svd[1], marker=9, s=80, label="mode", color='#0048ff')

for x, y in zip(mode_list_svd[0], mode_list_svd[1]) :
    ax[2][0].text(x=x+0.01, y=y+0.01, s=f"mode [{x}, {y}]", color='#0048ff', fontsize=10)


## ##### pic 2, 1
np_kmeans_label_svd, kmeans_centroid_list_svd = RUNNING_KMEANS(np_tcsvd_T, 3)

svd_ari = CALC_ARI_SCORE(predicted_lables=np_kmeans_label_svd, np_truth=np_truth_3d)

x_data = np_tcsvd_T[0]
y_data = np_tcsvd_T[1]

colors = np.array(['#9ac0e6', '#d6a6d3', '#fe7f0e'])
color_map = colors[np_kmeans_label_svd]

for x, y, c in zip(x_data, y_data, color_map) :
    ax[2][1].scatter(x=x, y=y, marker = 'o', s=60, alpha = 0.5, color=c)

ax[2][1].set_xlabel("SVD 1", fontsize=15)
ax[2][1].set_ylabel("SVD 2", fontsize=15)
ax[2][1].set_title("KMeans Clusterung set 3D to 2D SVD : 0.txt (n=500) (depth=125x)", fontsize=15)

cluster = [0, 1, 2]
legend_list = []

for j, color in zip(cluster, colors) :
    num_of_this_cluster= np.sum(np_kmeans_label_svd == j)
    legend_list.append(mpatches.Patch(color=color, label=f'KMeans Cluster {j} : {num_of_this_cluster}'))

ax[2][1].text(x= 0.05, y= 0.95 , s=f"ARI score : {svd_ari}", color = 'red' , fontsize = 15, transform=ax[2][1].transAxes,  verticalalignment='top', horizontalalignment='left')
ax[2][1].legend(handles=legend_list, title='KMeans Cluster', fontsize=10)

ax[2][1].scatter(x=kmeans_centroid_list_svd[0], y=kmeans_centroid_list_svd[1], marker='P', s=80, label="centroid", color='blue')
for x, y in zip(kmeans_centroid_list_svd[0], kmeans_centroid_list_svd[1]) :
    ax[2][1].text(x=x-0.01, y=y-0.01, s=f"Centroid [{x}, {y}]", color='blue', fontsize=10)
