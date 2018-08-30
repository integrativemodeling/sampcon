The results directory includes one directory per target complex (called TGT below, for e.g. 1AVX), containing:

Note that all files are stored in /salilab/park1/shruthi/sampcon/sample_4/TGT except the ones in folder `protocol_outputs`.

1. `TGT_4.1 and TGT_4.2`: the results of IMP/PMI sampling, two independent runs. Not stored on github for size issues.
2. `TGT.all_centers.zdock_closest.txt`: the closest cluster center from IMP sampling for each good-scoring ZDOCK model, and the corresponding distance (for Figure 4 in the paper) 
3. `TGT.complete_scores.out`: the scores of all sampled IMP models
4. `TGT.run[1-2]_scores.txt`,`TGT.runall_scores.txt`: the scores of selected good-scoring models in run1, run2 and combining run1 and run2.
5. `TGT.imp.12.0A.1.0p.xlink_good.txt`: the run id, replica id and frame id for good-scoring IMP models., `TGT.imp.xlink_distances.txt`: the crosslink distances of all sampled IMP models, from which good-scoring models are chosen and `id_runs.txt`:  good-scoring model number and the sample (1 or 2) it was taken from.
6. `modelset`:
This directory contains: 
	i) all good-scoring RMFs (numbered 0 onwards).
	ii) `TGT.all_vs_all_distances.pkl`: the distance matrix for RMSD calculation
	iii) `cluster_center_rmfs.txt`: the list of RMFs corresponding to cluster centers (used for checking proximity of ZDOCK models)
	iv) `precision_cluster_dirs`: the set of clusters obtained by clustering at the final cutoff, for visualization (should be higher than sampling precision). Each cluster has a directory containing models in the cluster (in the park1 location above). All clusters also have lists of models from run1, run2 and both runs belonging to the cluster. Also there is a file containing models which are cluster centers. 
	v) `precision_cluster_dirs_samplingprecision`: same format as above, except that these clusters are obtained by clustering at the sampling precision.
7. `protocol_outputs`:
	i)`TGT.precisions.txt`: contains the sampling and cluster precisions. 
	ii) `scoretests`: results of the first (TGT.topscore_convergence.txt: the last line is the worst score) and second score tests (TGT.UC.txt: U-statistic, p-value and effect size). 
	iii) `precision_vs_pvalue`: pvalue, Cramers V and population at each threshold
	iv) `population_run1_vs_run2`: populations and RMSFs of each cluster
	v) `densities`: density maps of each cluster  

# Info

_Author(s)_: Shruthi Viswanath, Ilan E. Chemmama 

_Maintainer_: `shruthivis`

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
- S. Viswanath, I.E.Chemmama, P. Cimmermancic and A. Sali, Assessing Exhaustiveness of Stochastic Sampling for Integrative Modeling of Macromolecular Structures, in press, Biophysical Journal, 13, 2344-2353, 2017.

