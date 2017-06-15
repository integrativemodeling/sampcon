import IMP
import RMF
import IMP.atom
import IMP.rmf
import os,sys,math,numpy
import pickle

###################### SYSTEM SETUP #####################
# Parameters to tweak
tgt = sys.argv[1]
numModels = int(sys.argv[2])
meth = sys.argv[3]

pklFile = tgt+'.'+meth+'.pkl' 

receptor_chain = "A"
receptor_color = "blue"

ligand_chain = "B"
ligand_color = "red"

ligand_coords=[]


for i in range(numModels):
    
    m=IMP.Model()
    mdl_i=str(i)+'.rmf3'
    
    # read each frame and store the ligand coords
    fh_i=RMF.open_rmf_file_read_only(mdl_i)
    
    hier_i=IMP.rmf.create_hierarchies(fh_i,m)[0]

    IMP.rmf.load_frame(fh_i, 0)
    
    for state_i in hier_i.get_children():
        for chain_i in state_i.get_children():
            if "B" in chain_i.get_name():
                ligand_coords_i=[IMP.core.XYZ(a).get_coordinates() for a in IMP.atom.get_leaves(chain_i)] 
    
    ligand_coords.append(ligand_coords_i)
    
    del m,hier_i

#STEP 1. Calculate the distance matrix
distmat=numpy.zeros((numModels,numModels))

for i in range(numModels-1):
    
    for j in range(i+1,numModels):
         dist=IMP.algebra.get_rmsd(ligand_coords[i],ligand_coords[j])
         distmat[i][j]=dist
    if i%100==0:
        print i
         
         
pickle.dump(distmat,open(pklFile,"wb"))


