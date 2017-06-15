#!/bin/bash

tgt=$1

threshold=$2

percent=$3

cd $tgt 

python ~/data/sampcon/scripts/choosing_by_xlinks/get_xlink_satisfied_models_imp.py $tgt'.imp.xlink_distances.txt' $threshold $percent $tgt'.imp.'$threshold'A.'$percent'p.xlink_good.txt'


cd ../
