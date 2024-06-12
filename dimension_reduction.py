from sklearn.decomposition import PCA, TruncatedSVD
import numpy as np
import pandas as pd


def PERFORM_SVD ( np_vaf ):
    tcsvd = TruncatedSVD(n_components=2)
    tcsvd.fit(np_vaf.T)
    np_tcsvd = tcsvd.transform(np_vaf.T)
    np_tcsvd_T = np_tcsvd.T
    return np_tcsvd_T

def PERFORM_PCA(np_vaf) :
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(np_vaf_3d.T)

    return principalComponents
