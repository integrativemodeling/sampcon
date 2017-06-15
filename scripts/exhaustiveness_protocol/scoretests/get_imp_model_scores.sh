#!/bin/bash

tgt=$1

cd $tgt
rm *scores* 

for runnum in 1 2 
do 
	for replicanum in `seq 0 3`
	do
		~/imp-clean/build/setup_environment.sh ~/imp-clean/imp/modules/pmi/pyext/src/process_output.py -f $tgt'_4.'${runnum}'/output/stat.'${replicanum}'.out' -s rmf_frame_index Total_Score | grep -v  ^'#' | awk -v rn="$runnum" -v rep="$replicanum" '{print rn,rep,$2,$3}' >> $tgt'.complete_scores.out'
	done	

done

#~/imp-clean/build/setup_environment.sh ~/imp-clean/imp/modules/pmi/pyext/src/process_output.py -f $tgt'_4.'$runnum'/output/stat.'$replicanum.out --search_field rmf_frame_index --search_value $rmf_frame | grep Total_Score | awk '{printf "%.2f" $2}' >> $tgt'.run'$runnum'_scores.txt'

python ~/data/sampcon/scripts/choosing_by_xlinks/scoredist/get_required_model_scores.py $tgt'.complete_scores.out' $tgt'.imp.12.0A.1.0p.xlink_good.txt' $tgt

cat $tgt'.run1_scores.txt'  $tgt'.run2_scores.txt' > $tgt'.runall_scores.txt'
cp *scores*.txt ~/data/sampcon/sample_4/figures/scoreconv/

cd ../

