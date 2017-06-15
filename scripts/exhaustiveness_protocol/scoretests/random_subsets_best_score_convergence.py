import numpy,string
import sys, os
import random

def get_scores_from_file(score_file):
    
    scores=[]
    sf=open(score_file,'r')
    
    for ln in sf.readlines():
        scores.append(float(ln.strip()))
        
    return scores


def get_random_score_set(scores_list,num_models):
    
    scores_chosen=[]
    score_indices_chosen=[]
    
    while len(scores_chosen)<num_models:
        
        newindex=random.randint(0,len(scores_list)-1)
        
        if newindex not in score_indices_chosen:
            score_indices_chosen.append(newindex)
            scores_chosen.append(scores_list[newindex])
            
    return scores_chosen

    
# Files with lists of scores from run1 and run2 
run1_scores_file=sys.argv[1]
run2_scores_file=sys.argv[2]

run1_scores=get_scores_from_file(run1_scores_file)
run2_scores=get_scores_from_file(run2_scores_file)

run_scores=run1_scores+run2_scores

replicates=10

numModels=len(run_scores)
randomSubsets=[int(0.2*numModels),int(0.4*numModels),int(0.6*numModels),int(0.8*numModels),numModels]

print "Subset","runboth_topscore_mean","runboth_topscore_stderr"

for r in randomSubsets:
    # for each random subset, get the mean top scoring model and the standard error
    
    topScores=[]
    
    for i in range(replicates):
        newTopScore=min(get_random_score_set(run_scores,r))
        
        topScores.append(newTopScore)
        
    topScores=numpy.array(topScores)
    
    
    print r,numpy.mean(topScores),numpy.std(topScores)/numpy.sqrt(float(len(topScores)))
    















