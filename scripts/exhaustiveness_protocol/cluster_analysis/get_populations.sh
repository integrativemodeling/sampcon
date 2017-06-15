#!/bin/bash

tgt=$1
outdir=~/data/sampcon/sample_4/figures/population_run1_run2

cd $tgt/modelset/precision_cluster_dirs

rm $outdir'/'$tgt'.population_run1_run2.txt'

num_models_run1=`wc -l ../../*run1_scores.txt | awk '{print $1}'`
num_models_run2=`wc -l ../../*run2_scores.txt | awk '{print $1}'`

echo $num_models_run1" "$num_models_run2

num_clusters=`ls *.all.txt |wc -l`

num_clusters_minus_1=`expr $num_clusters - 1`

for c in `seq 0 $num_clusters_minus_1`
do
	echo $c
	clus_run1=`wc -l cluster.$c'.run1.txt' | awk '{print $1}'`
	clus_run2=`wc -l cluster.$c'.run2.txt' | awk '{print $1}'`

	pop_run1=`wc -l cluster.$c'.run1.txt' | awk -v nr="$num_models_run1" '{print $1*100.0/nr}'`
	pop_run2=`wc -l cluster.$c'.run2.txt' | awk -v nr="$num_models_run2" '{print $1*100.0/nr}'`
	echo $clus_run1" "$clus_run2" "$pop_run1" "$pop_run2 >> $outdir'/'$tgt'.population_run1_run2.txt'
done

cd ../../../




