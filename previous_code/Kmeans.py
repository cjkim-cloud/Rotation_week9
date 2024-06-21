from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import numpy as np
import pandas as pd

def RUNNING_KMEANS(np_vaf, num_of_clusters):
    kmeans = KMeans(n_clusters=num_of_clusters, random_state=99)
    kmeans.fit(np_vaf.T)
    np_kmeans_label = np.where( kmeans.labels_ == 1, 0, np.where(kmeans.labels_== 2, 1, 2))
    kmeans_centroid_list = np.round(kmeans.cluster_centers_.T, 3)

    print("input argu ; num of cluster , np_vaf")
    print("output ; np_kmeans_label (i,)")

    return np_kmeans_label, kmeans_centroid_list

def CALC_ARI_SCORE(predicted_lables, np_truth) :
    cluster_result = predicted_lables
    true_labels = np_truth
    ari_score = round(adjusted_rand_score(true_labels, cluster_result) , 3)

    return ari_score
