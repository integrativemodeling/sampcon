#!/bin/bash

tgt=$1
rm -r ~/data/sampcon/sample_4/figures/densities/$tgt

mkdir ~/data/sampcon/sample_4/figures/densities/$tgt

precision=`grep $tgt tgt_cutoffs_visualization.txt | awk '{print $2}'`
echo $precision

cd $tgt/modelset/precision_cluster_dirs

num_clusters=`ls cluster*all.txt |wc -l`
num_clusters_minusone=`expr $num_clusters - 1`

for rnum in 1 2
do 
	for clus in `seq 0 $num_clusters_minusone`
	do 
		~/imp-clean/build/setup_environment.sh python ~/data/sampcon/scripts/densities/show_densities_given_model_list.py cluster.$clus'.run'$rnum'.txt' cluster.$clus $precision cluster$clus'_run'$rnum ~/data/sampcon/sample_4/figures/densities/$tgt ; done ; done

cd ../../../
