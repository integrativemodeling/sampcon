The directory contains the sampling script that uses IMP/PMI.

For each benchmark case 2  runs with 4 cores each were performed using the sampling script, as follows:

Example run:
mpirun -np 4 $IMPDIR/setup_environment.sh  python $SCRIPTSDIR/sample.py $TGT prod $INPUTSDIR
done 

The variables mentioned above refer to 
IMPDIR: IMP build directory
SCRIPTSDIR: directory where the sampling script is located
TGT: benchmark case PDB ID (e.g. 1AVX)
INPUTSDIR: directory where input PDBs and crosslinks for this case were stored

