import numpy as np
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import matplotlib.patches as mpatches
from sklearn.metrics import silhouette_samples, silhouette_score

import math

import Record_obj.py, scores.py, dimension_reduction.py

def CLUSTER_VISUALIZATION_1D(OUTPUT_DIR, NP_VAF_1D, cluster_hard_obj, NP_TRUTH=None) :

    # data setting    
    row = len(cluster_hard_obj)

    fig, ax = plt.subplots(row, 1, figsize=(5, 5 * row))
    color_candidates = np.array(["#d44252", "#fe7f0e", "#ffbf0e", "#19eb9a", "#94bdf7", "#0f6ac0", "#9880d7"])
    for n, trial in zip(range(len(cluster_hard_obj)), cluster_hard_obj) :
    
        legend_list = []

        x_data = NP_VAF_1D[0]
        y_data = np.zeros_like(x_data)

        colors = color_candidates[:trial.get_num_of_clusters()]
        color_map = colors[trial.get_membership()]

        for x, y, c in zip(x_data, y_data, color_map) :
            ax[n].plot(x, y, marker = 'o', alpha = 0.5, color=c)
        
        for j in range(trial.get_num_of_clusters()) :
            num_of_this_cluster= np.sum(trial.get_membership() == j)
            color = colors[j]
            legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))


        mixture_y_zero = np.zeros_like(trial.get_mixture())
        ax[n].legend(handles=legend_list, title='Cluster', fontsize=10)
    
        ax[n].plot(trial.get_mixture(), mixture_y_zero, marker='*' , label="centroid", color='red')

        for x, y in np.nditer([trial.get_mixture(), mixture_y_zero]):
            ax.text(x=x-0.01, y=y-0.005, s=f"mixture [{x:.2f}]", color='red', fontsize=8)

        ax[n].set_xlabel("vaf of Sample 1", fontsize=15)
        ax[n].set_title(f"1D data | K : {trial.get_num_of_clusters()}", fontsize=15)

    
        if NP_TRUTH is not None :
            print(CALC_ARI_SCORE(trial.get_membership(), NP_TRUTH))

        fig.savefig(OUTPUT_DIR+ f"/clustering_each_K_plot.png")
        
def CLUSTER_VISUALIZATION_2D(OUTPUT_DIR, NP_VAF_2D, cluster_hard_obj, NP_TRUTH=None) :

    # data setting    

    row = len(cluster_hard_obj)

    fig, ax = plt.subplots(row, 1, figsize=(6, 7 * row))
    
    color_candidates = np.array(["#d44252", "#fe7f0e", "#ffbf0e", "#19eb9a", "#94bdf7", "#0f6ac0", "#9880d7"])
    for n, trial in zip(range(len(cluster_hard_obj)), cluster_hard_obj) :
    
        legend_list = []

        x_data = NP_VAF_2D[0]
        y_data = NP_VAF_2D[1]

        
        colors = color_candidates[:trial.get_num_of_clusters()]
        color_map = colors[trial.get_membership()]

        for x, y, c in zip(x_data, y_data, color_map) :
            ax[n].plot(x, y, marker = 'o', alpha = 0.5, color=c)
        
        for j in range(trial.get_num_of_clusters()) :
            num_of_this_cluster= np.sum(trial.get_membership() == j)
            color = colors[j]
            legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))

        ax[n].legend(handles=legend_list, title='Cluster', fontsize=10)
    
        ax[n].scatter(trial.get_mixture()[0], trial.get_mixture()[1], marker='*' , label="centroid", color='red')

        for x, y in np.nditer([trial.get_mixture()[0], trial.get_mixture()[1]]):
            ax[n].text(x=x-0.01, y=y-0.005, s=f"mixture [{x:.3f}, {y:.3f}]", color='red', fontsize=8)

        ax[n].set_xlabel("vaf of Sample 1", fontsize=15)
        ax[n].set_ylabel("vaf of Sample 2", fontsize=15)
        ax[n].set_title(f"2D data | K : {trial.get_num_of_clusters()}", fontsize=15)

        if NP_TRUTH is not None :
            print(f"K : {trial.get_num_of_clusters()}, ARI : {CALC_ARI_SCORE(trial.get_membership(), NP_TRUTH)}")

        fig.savefig(OUTPUT_DIR+ f"/clustering_each_K_plot.png")

def CLUSTER_VISUALIZATION_3D(OUTPUT_DIR, NP_VAF_3D, cluster_hard_obj, NP_TRUTH=None) :

    NP_VAF_2D = PERFORM_PCA(NP_VAF_3D)

    # data setting    
    row = len(cluster_hard_obj)
    fig, ax = plt.subplots(row, 1, figsize=(6, 7 * row))
    color_candidates = np.array(["#d44252", "#fe7f0e", "#ffbf0e", "#19eb9a", "#94bdf7", "#0f6ac0", "#9880d7"])
    for n, trial in zip(range(len(cluster_hard_obj)), cluster_hard_obj) :
    
        legend_list = []
        x_data = NP_VAF_2D[0]
        y_data = NP_VAF_2D[1]

        
        colors = color_candidates[:trial.get_num_of_clusters()]
        color_map = colors[trial.get_membership()]

        for x, y, c in zip(x_data, y_data, color_map) :
            ax[n].plot(x, y, marker = 'o', alpha = 0.5, color=c)
        
        for j in range(trial.get_num_of_clusters()) :
            num_of_this_cluster= np.sum(trial.get_membership() == j)
            color = colors[j]
            legend_list.append(mpatches.Patch(color=color, label=f'Cluster {j} : {num_of_this_cluster}'))

        ax[n].legend(handles=legend_list, title='Cluster', fontsize=10)
    
        #ax[n].scatter(trial.get_mixture()[0], trial.get_mixture()[1], marker='*' , label="centroid", color='red')

        #for x, y in np.nditer([trial.get_mixture()[0], trial.get_mixture()[1]]):
            #ax[n].text(x=x-0.01, y=y-0.005, s=f"mixture [{x:.3f}, {y:.3f}]", color='red', fontsize=8)

        ax[n].set_xlabel("vaf of Sample 1", fontsize=15)
        ax[n].set_ylabel("vaf of Sample 2", fontsize=15)
        ax[n].set_title(f"3D to 2D data | K : {trial.get_num_of_clusters()}", fontsize=15)


         # 성능 테스트용
        if NP_TRUTH is not None :
            print(f"K : {trial.get_num_of_clusters()}, ARI : {CALC_ARI_SCORE(trial.get_membership(), NP_TRUTH)}")

        fig.savefig(OUTPUT_DIR+ f"/clustering_each_K_plot.png")




def CLUSTER_VISUALIZATION(OUTPUT_DIR, NP_VAF, cluster_hard_obj, DIMENSION, NP_TRUTH) :

    if DIMENSION == 1 :
        CLUSTER_VISUALIZATION_1D(OUTPUT_DIR, NP_VAF, cluster_hard_obj, NP_TRUTH)
    elif DIMENSION == 2:
        CLUSTER_VISUALIZATION_2D(OUTPUT_DIR, NP_VAF, cluster_hard_obj, NP_TRUTH)
    else: 
        CLUSTER_VISUALIZATION_3D(OUTPUT_DIR, NP_VAF, cluster_hard_obj, NP_TRUTH)
        

def OPTIMAL_K_VISUALIZATION(OUTPUT_DIR, DIMENSION, cluster_hard_obj) :
    
    gap_list =[]
    silhouette_list = []

    for trial in cluster_hard_obj :
        gap_list.append(trial.get_gap_score())
        silhouette_list.append(trial.get_silhouette_score())

    gap_list[gap_list == -np.inf] = np.nan
    masked_gap_list = np.ma.masked_invalid(gap_list)

    xlist = []
    for x in range(2, 8):
        xlist.append(x)

    fig, ax = plt.subplots(1,2, figsize=(10, 4))



    ax[0].set_title(f"Gap Statistics : {DIMENSION}D data")
    ax[0].scatter(xlist, masked_gap_list, color = "#94bdf7", linestyle='-', marker='o')
    ax[0].set_xlabel("K (num of clusters)")
    ax[0].set_ylabel("Gap score")

    ax[1].set_title(f"Silhouette Coefficient : {DIMENSION}D data")
    ax[1].plot(xlist, silhouette_list, color = "#edb2c2", linestyle='-', marker='o')
    ax[1].set_xlabel("K (num of clusters)")
    ax[1].set_ylabel("Silhouette Coefficient")

    fig.savefig(OUTPUT_DIR+ f"/{DIMENSION}_data_optimal_K_plot.png")





