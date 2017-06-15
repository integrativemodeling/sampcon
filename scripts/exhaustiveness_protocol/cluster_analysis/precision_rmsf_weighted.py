import IMP
import RMF
import IMP.atom
import IMP.rmf
import os,sys,math,numpy

import glob
###################### SYSTEM SETUP #####################
# Parameters to tweak

def compute_precision(path, tgt):
    conform=[]
    num=0
    weight = []
    for fl in glob.glob("%s/*.rmf3" % path):
        partcoord = []
        m = IMP.Model()
        inf = RMF.open_rmf_file_read_only(fl)
        h = IMP.rmf.create_hierarchies(inf, m)[0]
        IMP.rmf.load_frame(inf, 0)
      
        for state in h.get_children():
            for component in state.get_children():
                if tgt in component.get_name():
                    for leaf in IMP.core.get_leaves(component):
                        if len(IMP.atom.Fragment(leaf).get_residue_indexes()) == 0:
                            p=IMP.core.XYZ(leaf.get_particle())
                            partcoord.append(p.get_coordinates())
                            if num == 0:
                                weight.append(1.0)
                        else:
                            p=IMP.core.XYZ(leaf.get_particle())
                            partcoord.append(p.get_coordinates())
                            if num ==0:
                                weight.append(float(len(IMP.atom.Fragment(leaf).get_residue_indexes())))

        conform.append(partcoord)
        num += 1
        partcoord = []
    
        
    weight=numpy.array(weight)

    std = numpy.array(conform).std(0)*numpy.array(conform).std(0)
    
    Xs = numpy.sum(numpy.dot(std[:,0], weight)) 
    Ys = numpy.sum(numpy.dot(std[:,1], weight)) 
    Zs = numpy.sum(numpy.dot(std[:,2], weight))     
    return math.sqrt((Xs+Ys+Zs)/numpy.sum(weight))

path = str(sys.argv[1])
tgt="B"
print compute_precision(path, tgt)


