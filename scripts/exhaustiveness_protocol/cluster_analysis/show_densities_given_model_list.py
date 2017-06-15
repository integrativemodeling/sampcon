 
import IMP
import RMF
import IMP.atom
import IMP.rmf
import IMP.pmi
import IMP.pmi.tools
import IMP.pmi.topology
import IMP.pmi.dof
import IMP.pmi.macros
import IMP.pmi.restraints
import os,sys


model_list_file = sys.argv[1]
path_to_models = sys.argv[2]
precision_cutoff = float(sys.argv[3]) # precision threshold for calculating resolution of the MRC
mrc_file_prefix = sys.argv[4]
path_to_mrcs=sys.argv[5]

density_custom_ranges={"A":[("A")],"B":[("B")]}

# Setup macro

gmd = IMP.pmi.analysis.GetModelDensity(custom_ranges=density_custom_ranges,resolution=precision_cutoff)

mlf = open(model_list_file,'r')

for ln in mlf.readlines():
    model = IMP.Model()
    
    curr_rmf = path_to_models+"/"+ln.strip()+".rmf3"
    
    inf = RMF.open_rmf_file_read_only(curr_rmf)
    h = IMP.rmf.create_hierarchies(inf, model)[0] 
    
    gmd.add_subunits_density(h)

mlf.close()
gmd.write_mrc(path=path_to_mrcs,file_prefix=mrc_file_prefix)
