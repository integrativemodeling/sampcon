import IMP
import RMF
import IMP.atom
import IMP.rmf
import os,sys,math,numpy
import pickle

def get_model_list_from_file(model_list_file,model_dir):
    
    model_list = []
           
    mlf=open(model_list_file,'r')
    for ln in mlf.readlines():
        model_list.append(model_dir.rstrip("/")+"/"+ln.strip())
                     
    mlf.close()
    
    return (model_list)
   
       
def get_ligand_coords_zdock(model_list):
    ligand_coords=[]
    
    for mdl_name in model_list:
        m=IMP.Model()

        hier_i=IMP.atom.read_pdb(mdl_name,m,IMP.atom.CAlphaPDBSelector())
    
        ligand_i=hier_i.get_children()[1] 
   
        ligand_coords_i=[IMP.core.XYZ(a).get_coordinates() for a in IMP.atom.get_leaves(ligand_i)] 
        
        ligand_coords.append(ligand_coords_i)
        
        del m,hier_i

    return ligand_coords

def get_ligand_coords_imp(model_list):
    ligand_coords=[]
    
    for mdl_name in model_list:
        
        m=IMP.Model()

        # read each frame and store the ligand coords
        fh_i=RMF.open_rmf_file_read_only(mdl_name)
        
        hier_i=IMP.rmf.create_hierarchies(fh_i,m)[0]

        IMP.rmf.load_frame(fh_i, 0)
    
        for state_i in hier_i.get_children():
            for chain_i in state_i.get_children():
                if "B" in chain_i.get_name():
                    ligand_coords_i=[IMP.core.XYZ(a).get_coordinates() for a in IMP.atom.get_leaves(chain_i)] 
    
        ligand_coords.append(ligand_coords_i)
    
        del m,hier_i
    
    return ligand_coords

###################### SYSTEM SETUP #####################
# Parameters to tweak
zdock_models_list_file = sys.argv[1]
zdock_models_dir = sys.argv[2]
imp_models_list_file=sys.argv[3]
imp_models_dir = sys.argv[4]

zdock_model_list=get_model_list_from_file(zdock_models_list_file,zdock_models_dir)

zdock_ligands = get_ligand_coords_zdock(zdock_model_list)

imp_model_list=get_model_list_from_file(imp_models_list_file,imp_models_dir)

imp_ligands = get_ligand_coords_imp(imp_model_list)

for zi,zdock_lig in enumerate(zdock_ligands):
    
    mindist=1000000.0
 
    closest_model=-1
    
    for ii,imp_lig in enumerate(imp_ligands):
    
        dist=IMP.algebra.get_rmsd(imp_lig,zdock_lig)
        
        if dist<mindist:
            mindist=dist
            closest_model=imp_model_list[ii]

    print zdock_model_list[zi],closest_model,mindist


    
    


