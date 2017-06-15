#!/bin/bash

tgt=$1

scriptsDir=$HOME/data/sampcon/scripts/zdock
inputPdbDir=$HOME/data/sampcon/inputpdbs
transFile=$HOME/data/sampcon/decoys_bm4_zd3.0.2_6deg_fixed/results/$tgt'.zd3.0.2.fg.out'

mkdir zdock
cd zdock

	#link create.pl and create_lig into tgt dir

	ln -s $scriptsDir'/create.pl' create.pl

	ln -s $scriptsDir'/create_lig' create_lig

	ln -s $inputPdbDir'/'$tgt'_r_u.pdb' $tgt'_r_u.pdb.ms'

	ln -s $inputPdbDir'/'$tgt'_l_u.pdb' $tgt'_l_u.pdb.ms'

	./create.pl $transFile 


