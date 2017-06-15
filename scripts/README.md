The scripts directory contains the following scripts:

1. `sample`: script used for running sampling (replica exchange MC) on the 5 benchmark cases.
See also README.md in sample directory.

2.  `exhaustiveness_protocol`: run all exhaustiveness tests from the output of sampling.
    a. `prep`: 
        i) First run `get_xlink_distances.sh TGT` to get the crosslink distances for every sampled model, to identify good-scoring models. This provides the file `TGT.imp.xlink_distances.txt`. Note that the method of selecting good-scoring models varies based on the application. 
        ii) Next, run `get_xlink_satisfied_models.sh TGT THRESHOLD PERCENT` to get all the models from TGT that had PERCENT% of crosslinks within THRESHOLD. (Values were THRESHOLD=12.0 and PERCENT=1.0 in the paper). This outputs file `TGT.imp.12.0A.1.0p.xlink_good.txt` 
        iii) Finally extract the good scoring model RMFs using `collect_good_scoring_models.sh TGT`, which provides the good scoring models in the directory modelset and also a file `id_runs.txt` mapping the good-scoring model RMF to the sample(run) it came from.

    b. `scoretests`:
        i) Use `get_imp_model_scores.sh TGT` to get the scores of good-scoring models. Outputs are TGT.run1.scores, TGT.run2.scores and TGT.runall.scores.
        ii) Then get the convergence of the best score using `random_subsets_best_score_convergence.py TGT.run1.scores TGT.run2.scores`, which provides `TGT.topscore_convergence.txt`
        iii) Then get the results of the Mann-Whitney U test using `MannWhitney.py` which provides the U-statistic, p-value and effect size from the test.

    c. `precision_vs_pvalue`:
        i) First get the pairwise distance matrix of all good-scoring models using `get_all_vs_all_rmsd.py TGT NUMMODELS METHOD`,  where NUMMODELS is the number of good-scoring models for the case and METHOD is some arbitrary name for the file.  The result is a pickle file that stores the numpy distance matrix.
        ii) Then use `pp_wrapper_full.sh TGT` or the python script it references to get the list of p-values, Cramers V and populations for each threshold. This should provide the sampling precision by looking at the data. 
    d. `cluster_analysis`:
        i) Clustering can be done at the sampling precision or a worse precision. This is done using `get_clusters_wrapper.sh TGT PRECISION` where PRECISION is the cluster precision. This provides `precision_cluster_dirs`, the result of clustering at the cluster precision.
        ii) Calculate the RMSF of the resulting clusters using `precision_rmsf_wrapper.sh TGT`and the population of clusters using `get_population.sh TGT`.
        iii) Get cluster densities using `get_densities_wrapper.sh TGT`. 
 
3. `zdock`: To compare to ZDOCK, 
    a. first extract the PDBs of all the models as specified in the ZDOCK README. For e.g. this is done in `create_zdock_decoys.sh TGT`
    b. get the good-scoring ZDOCK models using first, `get_xlink_distances.py TGT 1 54000 TGT.xlinks > TGT.zdock.xlink_distances.out`, where 1 and 54000 are the starting and ending model IDs and `TGT.xlinks` is the crosslinks list for the complex (found in `inputs`). This provides the crosslink distances for all models in `TGT.zdock.xlink_distances.txt`, from which the list of good-scoring models is extracted similar to IMP, using `get_xlink_satisfied_zdock_models.py  TGT.zdock.xlink_distances.txt THRESHOLD PERCENT TGT.zdock.12.0A.1.0p.xlink_good.txt`
    c. Compare to IMP cluster centers using `compare_zdock_imp.sh TGT METHOD`, where METHOD is an arbitrary name for the output file. The output file is 	`TGT.METHOD.zdock_closest.txt` which contains distances from the ZDOCK model to the nearest IMP cluster center. 


4. `plot`: Gnuplot scripts to plot results of the protocol.

# Info

_Author(s)_: Shruthi Viswanath, Ilan E. Chemmama 

_Maintainer_: `shruthivis,ichem001`

_License_: [LGPL](http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

_Publications_:
- S. Viswanath, I.E.Chemmama, P. Cimmermancic and A. Sali, Validating Exhaustiveness of Stochastic Sampling for Integrative Modeling of Macromolecular Structures, submitted.

