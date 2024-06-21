class Step :
    def __init__(self, membership, theta, mixture, distance_inertia, step_index, num_of_clusters, silhouette_score=None, gap_score=None) :
        self.membership = membership
        self.theta = theta
        self.mixture = mixture
        self.distance_inertia = distance_inertia
        self.step_index = step_index
        self.num_of_clusters = num_of_clusters
        self.silhouette_score = silhouette_score
        self.gap_score = gap_score


    def get_membership(self) :
        return self.membership
    
    def get_theta(self) :
        return self.theta
    
    def get_mixture(self) :
        return self.mixture
        
    def get_distance_inertia(self) :
        return self.distance_inertia
    
    def get_step_index(self) :
        return self.step_index
    
    def get_ari_score(self) :
        return self.ari_score
    
    def get_num_of_clusters(self) :
        return self.num_of_clusters
    
    def get_silhouette_score(self) :
        return self.silhouette_score
    
    def get_gap_score(self) :
        return self.gap_score

    def copy_to_trial_obj(self) :
        trial = Trial(self.membership, self.theta, self.mixture, self.distance_inertia, self.num_of_clusters, self.silhouette_score, self.gap_score)
        return trial


    def set_silhouette_score(self, silhouette_score) :
        self.silhouette_score = silhouette_score

    def set_gap_score(self, gap_score) :
        self.gap_score = gap_score
    
class Trial :
    def __init__(self, membership, theta, mixture, distance_inertia,  num_of_clusters, silhouette_score=None, gap_score=None) :
        self.membership = membership
        self.theta = theta
        self.mixture = mixture
        self.distance_inertia = distance_inertia
        self.num_of_clusters = num_of_clusters 
        self.silhouette_score = silhouette_score
        self.gap_score = gap_score
    
    
    def get_membership(self) :
        return self.membership
    
    def get_theta(self) :
        return self.theta
    
    def get_mixture(self) :
        return self.mixture
        
    def get_distance_inertia(self) :
        return self.distance_inertia
        
    
    def get_num_of_clusters(self) :
        return self.num_of_clusters
    
    def get_silhouette_score(self) :
        return self.silhouette_score
    
    def get_gap_score(self) :
        return self.gap_score
    

    def set_silhouette_score(self, silhouette_score) :
        self.silhouette_score = silhouette_score

    def set_gap_score(self, gap_score) :
        self.gap_score = gap_score

    
class Cluster_hard :
    def __init__(self) :
        self.cluster_hard = []

    def append(self, trial) :
        self.cluster_hard.append(trial)

    def return_cluster_hard(self) :
        return self.cluster_hard
        

