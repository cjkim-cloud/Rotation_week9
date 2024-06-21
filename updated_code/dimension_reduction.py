from sklearn.decomposition import PCA, TruncatedSVD


def PERFORM_PCA(NP_VAF_3D) :
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(NP_VAF_3D.T)

    return principalComponents.T

def PERFORM_SVD ( NP_VAF_3D):
    tcsvd = TruncatedSVD(n_components=2)

    tcsvd.fit(NP_VAF_3D.T)
    np_tcsvd = tcsvd.transform(NP_VAF_3D.T)

    np_tcsvd_T = np_tcsvd.T
    return np_tcsvd_T

