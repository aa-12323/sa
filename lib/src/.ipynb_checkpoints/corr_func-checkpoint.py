import treecorr


def get_ng(cluster,mode1,mode2):
    if mode2=="abs":
        UPPER_BOUND=np.max(shapes[('All','R')])
        distance=('All','angR')
        
    elif mode2=="rel":
        UPPER_BOUND=1.2
        distance=('All','normLR')
    else:
        raise

    if mode1 == "s":
        def get_cluster_cen(cluster):
            return (get_unique_center_for_cluster(cluster))
        def get_cluster_sats(cluster):
            cen_mat_id=cluster.name
            cen_id=cluster[('Alt','Alt1','ID_CENT')]
            

            
                
            sats=members[members['All','MEM_MATCH_ID']==cen_mat_id]
                         
            sats=sats[sats.index!=cen_id]
            return (sats)
    elif mode1=='r':
        def get_cluster_sats(cluster):
            return(shapes)
        def get_cluster_cen(cluster):
            return (random)

    else:
        raise


    cen=get_cluster_cen(cluster)
    sats=get_cluster_sats(cluster)
    

    sats_e1=sats[('All','e1')].to_numpy()
    sats_e2=sats[('All','e2')].to_numpy()
    sats_angr=sats[distance]

#     print(sats_e1,sats_e2)

    if type(cen[('All','RA')])==np.float64:
        cen_angr=np.array(cen[distance]).reshape(1)
        cen_ra=np.array(cen[('All','RA')]).reshape(1)
        cen_dec=np.array(cen[('All','DEC')]).reshape(1)
    else:
#         cen_e1=cen[('All','e1')].to_numpy
#         cen_e2=cen[('All','e2')].to_numpy()
        cen_angr=cen[distance].to_numpy()
        cen_ra=cen[('All','RA')].to_numpy()
        cen_dec=cen[('All','DEC')].to_numpy()




#     print(cen_e1,cen_e2)

    sats_ra=sats[('All','RA')].to_numpy()
    sats_dec=sats[('All','DEC')].to_numpy()




#     print(np.shape(cen_ra),np.shape(cen_dec))    
#     print(cen_ra,cen_dec)    

    sats_cat = treecorr.Catalog( g1 = sats_e1, g2   = sats_e2, 
                                 ra = sats_ra, dec = sats_dec,r=sats_angr,
                                 ra_units='deg', dec_units='deg')

    cen_cat = treecorr.Catalog( 
                                 ra = cen_ra, dec = cen_dec, r=cen_angr,
                                 ra_units='deg', dec_units='deg')
    
    MINSEP=0.01
    BINSLOP=0
        

    ng = treecorr.NGCorrelation(nbins=NBINS, min_sep=MINSEP, max_sep=UPPER_BOUND, bin_slop=BINSLOP,
                               metric="Rperp")
    ng.process_cross(cen_cat,sats_cat)

    return(ng)






def get_ng_list(mode2,source):
    length=len(clusters)
    ng_list=np.empty([length,4,NBINS])
    filler=np.zeros([1,4,NBINS])

    i=0
    e_count=0
    for index,cluster in tqdm(clusters.iterrows()):
        try:
            ng_list[i,:,:]=get_xi_meanlogr_varxi_npairs(cluster,'s',mode2,source)
            i=i+1
        except ValueError as e:
            ng_list[i,:,:]=filler
            i=i+1
            e_count=e_count+1
    print("Number of empty sat catalogs is {}".format(e_count))
    return (ng_list)
    
    
    
def get_xi_meanlogr_varxi_npairs(cluster,mode1,mode2,source):
    ng=get_ng(cluster,mode1,mode2,source)
    return(np.array([ng.xi,ng.meanlogr,ng.varxi,ng.npairs]))

def get_sum(ng_list):
    sum_xi_cross=np.sum(ng_list[:,0,:],axis=0)
    sum_meanlogr=np.sum(ng_list[:,1,:],axis=0)
    sum_npairs=np.sum(ng_list[:,3,:],axis=0)
    return(sum_xi_cross,sum_meanlogr,sum_npairs)

def get_mean(ng_list):
    sum_xi_cross=np.sum(ng_list[:,0,:],axis=0)
    sum_meanlogr=np.sum(ng_list[:,1,:],axis=0)
    sum_npairs=np.sum(ng_list[:,3,:],axis=0)
    return(sum_xi_cross/sum_npairs,sum_meanlogr/sum_npairs)

def get_sigma(ng_list):
    xi_array=ng_list[:,0,:]
    npairs_array=ng_list[:,3,:]
    
    N=len(xi_array)
    
    jk_xi_array=np.empty([N,NBINS])
    
    def get_xi(drop_1_xi,drop_1_npairs):
        return(np.sum(drop_1_xi,axis=0)/np.sum(drop_1_npairs,axis=0))
    
    for i in range(N):
        drop_1_xi=np.delete(xi_array,i,axis=0)
        drop_1_npairs=np.delete(npairs_array,i,axis=0)
        jk_xi_array[i,:]=get_xi(drop_1_xi,drop_1_npairs)
        
    return(np.sqrt(N)*np.std(jk_xi_array,axis=0))


def get_ng_source(clusters,sources,z_lower,z_upper,lambda_lower,lambda_upper,foreback,woRed=False):
    clusters_z_masked=clusters[(clusters[('All','All','Z_LAMBDA')]>=z_lower)&(clusters[('All','All','Z_LAMBDA')]<=z_upper)]
    clusters_lambda_masked=clusters[(clusters[('All','All','LAMBDA_CHISQ')]>=lambda_lower)&(clusters[('All','All','LAMBDA_CHISQ')]<=lambda_upper)]
    
    if woRed==True:
        sources=sources[woRedMask]
    
    print("The number of sources is {}".format(len(sources)))
    
    center_id=clusters_z_masked[('Alt','Alt1','ID_CENT')]
    centers=members.loc[center_id]
    
    
    UPPER_BOUND=10
    distance=('All','angR')


#     if mode1 == "s":
#         def get_cluster_cen(cluster):
#             return (get_unique_center_for_cluster(cluster))
#         def get_cluster_sats(cluster):
#             cen_mat_id=cluster.name
#             cen_id=cluster[('Alt','Alt1','ID_CENT')]
            

            
#             if source==True:
#                 sats=members
                
#             else: 
#                 sats=members[members['All','MEM_MATCH_ID']==cen_mat_id]
                         
#             sats=sats[sats.index!=cen_id]
#             return (sats)
#     elif mode1=='r':
#         def get_cluster_sats(cluster):
#             return(shapes)
#         def get_cluster_cen(cluster):
#             return (random)

#     else:
#         raise


    cen=centers
    sats=members
    
    if foreback=="back":
        print("Calculating background sources")
        sats=sats[(sats[('All','mean_z')]-z_upper)>=0.1]
    elif foreback=="fore":
        sats=sats[(z_lower-sats[('All','mean_z')])>=0.1]
        print("Calculating foreground sources")
        print(sats[('All','mean_z')].mean())
        print(len(sats))

    sats_e1=sats[('All','e1')].to_numpy()
    sats_e2=sats[('All','e2')].to_numpy()
    sats_angr=sats[distance]

#     print(sats_e1,sats_e2)

    if type(cen[('All','RA')])==np.float64:
        cen_angr=np.array(cen[distance]).reshape(1)
        cen_ra=np.array(cen[('All','RA')]).reshape(1)
        cen_dec=np.array(cen[('All','DEC')]).reshape(1)
    else:
#         cen_e1=cen[('All','e1')].to_numpy
#         cen_e2=cen[('All','e2')].to_numpy()
        cen_angr=cen[distance].to_numpy()
        cen_ra=cen[('All','RA')].to_numpy()
        cen_dec=cen[('All','DEC')].to_numpy()




#     print(cen_e1,cen_e2)

    sats_ra=sats[('All','RA')].to_numpy()
    sats_dec=sats[('All','DEC')].to_numpy()




#     print(np.shape(cen_ra),np.shape(cen_dec))    
#     print(cen_ra,cen_dec)    

    sats_cat = treecorr.Catalog( g1 = sats_e1, g2   = sats_e2, 
                                 ra = sats_ra, dec = sats_dec,r=sats_angr,
                                 ra_units='deg', dec_units='deg')

    cen_cat = treecorr.Catalog( 
                                 ra = cen_ra, dec = cen_dec, r=cen_angr,
                                 ra_units='deg', dec_units='deg')
    
    MINSEP=0.1
    BINSLOP=0.1
        

    ng = treecorr.NGCorrelation(nbins=NBINS, min_sep=MINSEP, max_sep=UPPER_BOUND, bin_slop=BINSLOP,
                               metric="Rperp")
    ng.process(cen_cat,sats_cat)

    return(ng)
