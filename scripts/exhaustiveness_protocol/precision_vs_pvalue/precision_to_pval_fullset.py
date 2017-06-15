import os,sys,random,numpy,math
import scipy.stats
import pickle

def get_run_identity(runid_file):
    # whether a run belongs to run1 or run2
        
    run1_models=[]
    run2_models=[]
    sf=open(runid_file,'r')

    for ln in sf.readlines():
        
        fields=ln.strip().split()
        modelid=int(fields[0])-1
        runid=int(fields[1])
        
        if runid==1:
            run1_models.append(modelid)
        elif runid==2:
            run2_models.append(modelid)
    
    sf.close()
   
    return run1_models,run2_models

def get_cutoffs_list(distmat,gridSize,numModels):

	maxdist=0.0
	mindist=1000000.0
	for i in range(numModels-1):
    		for j in range(i+1,numModels):
        		if distmat[i][j]>maxdist:
            			maxdist=distmat[i][j]

        		if distmat[i][j]<mindist:
           			 mindist=distmat[i][j]

	cutoffs=numpy.arange(mindist,maxdist,gridSize) # or maxdist/2.0, 5.0 s

	return cutoffs

def precision_cluster(distmat,numModels,rmsd_cutoff):
    #STEP 2. Populate the neighbors ofa given model
    neighbors=[]
    for count in range(numModels):
        neighbors.append([count])  # model is a neighbor of itself
 
    for i in range(numModels-1):
        for j in range(i+1,numModels):
        
            if distmat[i][j]<=rmsd_cutoff: # accepted to be a neighbor
                #print i,j,distmat[i][j]

                neighbors[i].append(j)
                neighbors[j].append(i)
     
    #STEP 3. Get the weightiest cluster, and iterate
    unclustered=[]
    boolUnclustered=[]
    for i in range(numModels):
        unclustered.append(i)
        boolUnclustered.append(True)

    cluster_members=[] # list of lists : one list per cluster
    cluster_centers=[]

    while len(unclustered)>0:
        # get cluster with maximum weight
        max_neighbors=0
        currcenter=-1
        for eachu in unclustered:  # if multiple clusters have same maxweight this tie is broken arbitrarily! 
            if len(neighbors[eachu])>max_neighbors:
                max_neighbors=len(neighbors[eachu])
                currcenter=eachu   
   
        #form a new cluster with u and its neighbors
        cluster_centers.append(currcenter)
        cluster_members.append([n for n in neighbors[currcenter]]) 

        #update neighbors 
        for n in neighbors[currcenter]:
            #removes the neighbor from the pool
            unclustered.remove(n) #first occurence of n is removed. 
            boolUnclustered[n]=False # clustered

        for n in neighbors[currcenter]:
            for unn in neighbors[n]: #unclustered neighbor
                if not boolUnclustered[unn]:
                    continue
                neighbors[unn].remove(n)
   
    return cluster_centers,cluster_members

def get_contingency_table(num_clusters,cluster_members,models_subset,run1_models,run2_models):

	full_ctable=numpy.zeros((num_clusters,2))
		
	for ic,cluster in enumerate(cluster_members):
		for member in cluster:
			model_index=models_subset[member]

			if model_index in run1_models:
                                #print "run1",model_index
                                full_ctable[ic][0]+=1.0
			elif model_index in run2_models:
				#print "run2",model_index
                                full_ctable[ic][1]+=1.0

	## now normalize by number of models in each run
	numModelsRun1 = float(numpy.sum(full_ctable,axis=0)[0])
	numModelsRun2 = float(numpy.sum(full_ctable,axis=0)[1])

  	reduced_ctable=[]
	
	retained_clusters=[]

	for i in range(num_clusters):
		if full_ctable[i][0]<=10.0 or full_ctable[i][1]<=10.0:
			continue
		reduced_ctable.append([full_ctable[i][0],full_ctable[i][1]])
		retained_clusters.append(i)

	return numpy.array(reduced_ctable),retained_clusters

def test_sampling_convergence(contingency_table,total_num_models):

    if len(contingency_table)==0:
        return 0.0,1.0

    ct = numpy.transpose(contingency_table) 
    
    [chisquare,pvalue,dof,expected]=scipy.stats.chi2_contingency(ct)
    
    if dof==0.0:
            cramersv=0.0 #converged, one single cluster
    else:
            cramersv=math.sqrt(chisquare/float(total_num_models))
   
             
    return(pvalue,cramersv)

def percent_ensemble_explained(ctable,total_num_models):
       
        if len(ctable)==0:
            return 0.0
        percent_clustered=float(numpy.sum(ctable,axis=0)[0]+numpy.sum(ctable,axis=0)[1])*100.0/float(total_num_models)
        
        return percent_clustered

# each run of this script gives, for a randoms subset of num_models_needed, the p-value 
tgt=sys.argv[1]
runid_file=sys.argv[2] # gives the run identity for a cluster
pklFile=sys.argv[3]

# parameters to set
gridSize=2.5

# get the model index of run1 and run2 models separately
run1_all_models,run2_all_models=get_run_identity(runid_file)

all_models=run1_all_models+run2_all_models

total_num_models=len(all_models)

# get cutoffs from all vs all distances
distmat_full=pickle.load(open(pklFile,"rb"))

cutoffs_list=get_cutoffs_list(distmat_full,gridSize,total_num_models)

for c in cutoffs_list:
       cluster_centers,cluster_members=precision_cluster(distmat_full,total_num_models,c)

       ctable,retained_clusters=get_contingency_table(len(cluster_centers),cluster_members,all_models,run1_all_models,run2_all_models)
       (pval,cramersv)=test_sampling_convergence(ctable,total_num_models)

       percent_explained= percent_ensemble_explained(ctable,total_num_models)

       print c,pval,cramersv,percent_explained

   
