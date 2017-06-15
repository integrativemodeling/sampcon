#!/bin/bash
	tgt=$1
	precision=$2
	echo $precision
	cd $tgt/modelset

	mv precision_cluster_dirs precision_cluster_dirs_samplingprecision 

	python ~/data/sampcon/scripts/choosing_by_xlinks/cluster/precision_to_pval_final.py $tgt ../id_runs.txt $tgt.all_vs_all_distances.pkl $precision 

	num_clusters=`ls cluster.*.all.txt|wc -l`
	num_clus_minus_one=`echo $num_clusters | awk '{print $1-1}'`

	for c in `seq 0 $num_clus_minus_one`
	do
	        echo $c	
		mkdir cluster.$c
		for mdl in `cat cluster.$c'.all.txt'`
		do
			cp $mdl.rmf* cluster.$c
		done

	done

	mkdir precision_cluster_dirs
	mv cluster.* cluster_centers*  precision_cluster_dirs


