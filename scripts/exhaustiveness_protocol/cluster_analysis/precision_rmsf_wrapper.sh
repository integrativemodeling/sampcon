#!/bin/bash

tgt=$1
cd $tgt

cd modelset/precision_cluster_dirs

outfile=~/data/sampcon/sample_4/figures/population_run1_run2/$tgt'.rmsfs'
rm $outfile

for dr in `ls -d cluster.*/`
do 

rmsf=`~/imp-clean/build/setup_environment.sh python  ~/data/sampcon/scripts/choosing_by_xlinks/cluster/precision_rmsf_weighted.py $dr`
echo $dr" "$rmsf >> $outfile

done 

cd ../../../
