def get_unique_center_for_cluster(cluster,member=0):
    centers=shapes.loc[cluster[('Alt','Alt1','ID_CENT')]]
    if type(centers)==pd.core.frame.DataFrame:
        if member==0:
            centers=centers.iloc[1]
        if member!=0:
            centers=centers[centers['MEM_MATCH_ID']==member['MEM_MATCH_ID']]
    elif type(centers)==pd.core.series.Series:
        pass
    else:
        raise TypeError
    
    return(centers)

def get_cluster_for_member(clusters,member):
    cluster_id=member[('All','MEM_MATCH_ID')]
    cluster=clusters.loc[cluster_id]
    return(cluster)