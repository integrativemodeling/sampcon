#!/bin/bash

tgt=$1

cd $tgt 

# STEP 1. Get all the distances of different crosslinks in each model in the format rmf frame_num dist1 dist2 ..
xlinkFields=`~/imp-clean/imp/modules/pmi/pyext/src/process_output.py -f $tgt'_4.1/output/stat.0.out' -p | grep CrossLinkingMassSpectrometryRestraint_Distance_ | tr "\n" " "`

rm $tgt'.imp.xlink_distances.txt'

for run in `seq 1 2`
do 
	for replica in `seq 0 3`
	do
		rm runids temp temp2
		~/imp-clean/imp/modules/pmi/pyext/src/process_output.py -f $tgt'_4.'$run'/output/stat.'$replica'.out' -s "rmf_frame_index" $xlinkFields > temp

		grep -v ^'#' temp | awk '{for(i=2;i<=NF;i++) {printf $i" ";} printf "\n";}' > temp2
		
		numLines=`wc -l temp2 | awk '{print $1}'`
		echo $numLines

		for i in `seq 1 $numLines`
		do 
			echo $run" "$replica >> runids
		done

		paste runids temp2 >> $tgt'.imp.xlink_distances.txt'
	done
done

rm runids temp temp2

