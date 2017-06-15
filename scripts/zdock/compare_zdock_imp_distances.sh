#!/bin/bash

tgt=$1
meth=$2

cd $tgt

#ls *.rmf3 > imp_models_list

cat modelset/precision_cluster_dirs/cluster_centers.txt | xargs -i echo {}'.rmf3' > modelset/cluster_center_rmfs.txt

rm $tgt'.'$meth'.zdock_closest.txt' 

~/imp-clean/build/setup_environment.sh python ~/data/sampcon/scripts/choosing_by_xlinks/zdock/get_closest_imp_model.py ~/data/sampcon/sample_3/$tgt/zdock/$tgt'.zdock.12.0A.1.0p.xlink_good.txt' ~/data/sampcon/sample_3/$tgt/zdock/pdbs modelset/cluster_center_rmfs.txt modelset >> $tgt'.'$meth'.zdock_closest.txt'

cd ../




