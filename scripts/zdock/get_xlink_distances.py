import IMP
import RMF
import IMP.atom
import IMP.rmf
import os,sys,math,numpy
import pickle

###################### SYSTEM SETUP #####################
# Parameters to tweak
tgt = sys.argv[1]
mdlStart=int(sys.argv[2])
mdlEnd = int(sys.argv[3])
xlinkFile=sys.argv[4]


# Step 1. Get the xlinks in the structure
xlinksList=[]

xlf= open(xlinkFile,'r')
for ln in xlf.readlines():
    if ln.startswith("res"):
        continue
    fields=ln.strip().split(',')
    xlinksList.append((int(fields[0]),fields[1],int(fields[2]),fields[3]))

xlf.close()


# Step 2. For each model get the xlink distances
for i in range(mdlStart,mdlEnd+1):
    m = IMP.Model()
    pdb_i='model.'+str(i)+'.pdb'
    modelpdb=IMP.atom.read_pdb(pdb_i,m)
    
    print pdb_i,

    for (res1,prot1,res2,prot2) in xlinksList:
    
        ra=IMP.atom.Selection(modelpdb,chain_id=prot1,atom_type=IMP.atom.AtomType("CA"),residue_index=int(res1)).get_selected_particles()[0]
        coorda = IMP.core.XYZ(ra)
    
    
        lb=IMP.atom.Selection(modelpdb,chain_id=prot2,atom_type=IMP.atom.AtomType("CA"),residue_index=int(res2)).get_selected_particles()[0]
        coordb = IMP.core.XYZ(lb)

        dist = IMP.core.get_distance(coorda,coordb)
        
        print "%.2f" %(dist),
    
    print
    
    del m,modelpdb
    
    # Much slower way of doing the above
    ## read each frame and store the ligand coords
    #hier_i=IMP.atom.read_pdb(pdb_i,mdl_i,IMP.atom.CAlphaPDBSelector())

    #receptor_i=hier_i.get_children()[0]
    #ligand_i=hier_i.get_children()[1] 
    
    #print pdb_i,
    #for r in IMP.atom.get_leaves(receptor_i):
        #ratom=IMP.atom.Atom(r)
        
        #for l in IMP.atom.get_leaves(ligand_i):
            #latom=IMP.atom.Atom(l)
            
            #tup=(IMP.atom.Residue(ratom.get_parent()).get_index(),"A",IMP.atom.Residue(latom.get_parent()).get_index(),"B")
   
            #if tup in xlinksList:
                
                #rcoord=IMP.core.XYZ(ratom)
                
                #lcoord=IMP.core.XYZ(latom)
                
                #dist=IMP.core.get_distance(rcoord,lcoord)
                
                #print "%.2f" %(dist),

    #print 
