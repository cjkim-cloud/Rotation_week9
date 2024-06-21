from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


def PERFORM_KMEANS(NP_VAF, num_of_clusters, max_iteration=20):
    kmeans = KMeans(n_clusters=num_of_clusters, init='k-means++', max_iter=max_iteration)
    kmeans.fit(NP_VAF.T)
    kmeans_centroid_list = np.round(kmeans.cluster_centers_.T, 5)

    return kmeans.labels_, kmeans_centroid_list
