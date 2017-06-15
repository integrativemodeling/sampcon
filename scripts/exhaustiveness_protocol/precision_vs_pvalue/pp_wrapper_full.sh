#!/bin/bash

tgt=$1
	cd $tgt/modelset

		
	cutoff=2.5

	rm ~/data/sampcon/sample_4/figures/precision_vs_pvalue/$tgt.$cutoff.full.prec_pval.txt
	
	python ~/data/sampcon/scripts/choosing_by_xlinks/cluster/precision_to_pval_fullset.py $tgt ../id_runs.txt $tgt'.all_vs_all_distances.pkl' >>  ~/data/sampcon/sample_4/figures/precision_vs_pvalue/$tgt.$cutoff.full.prec_pval.txt 

