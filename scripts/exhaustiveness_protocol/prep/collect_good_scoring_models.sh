#!/bin/bash

tgt=$1


cd $tgt 

mkdir modelset

rm id_runs.txt

# STEP 3. Use rmf_slice to actually get the models 
i=0
while read ln
do
	runnum=`echo $ln | awk '{print $1}'`
	replica=`echo $ln | awk '{print $2}'`
	framenum=`echo $ln | awk '{print $3}'`

	echo $runnum" "$replica" "$framenum

	~/imp-clean/build/bin/rmf_slice $tgt'_4.'$runnum'/output/rmfs/'$replica'.rmf3'  modelset/$i'.rmf3' --frame $framenum

	i=`expr $i + 1`

	echo $i" "$runnum >> id_runs.txt
done < $tgt'.imp.12.0A.1.0p.xlink_good.txt'



cd ../
