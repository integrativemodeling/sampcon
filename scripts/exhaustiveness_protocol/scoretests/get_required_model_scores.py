import numpy,string
import sys, os
import random

all_scores_file=sys.argv[1]

required_rmfs_file=sys.argv[2]

tgt=sys.argv[3]
outfile_run1=tgt+'.run1_scores.txt'

outfile_run2=tgt+'.run2_scores.txt'

needed_rmfs=[]

rrf=open(required_rmfs_file,'r')
for ln in rrf.readlines():
    curr_rmf=tuple([int(s) for s in ln.strip().split()]) # format: run, replica, rmf_frame_index
  
    needed_rmfs.append(curr_rmf)
    
rrf.close()

asf=open(all_scores_file,'r')

out1=open(outfile_run1,'w')
out2=open(outfile_run2,'w')

for ln in asf.readlines():
    rmf_file_id=tuple([int(s) for s in ln.strip().split()[0:3]])
    
    if rmf_file_id not in needed_rmfs:
        continue
    
    score=float(ln.strip().split()[3])
        
    if rmf_file_id[0]==1:
        print >>out1,"%.3f" %(score)
    elif rmf_file_id[0]==2:
        print >>out2,"%.3f" %(score)
        
out1.close()
out2.close()
asf.close()
    
    












