import sys, os
import scipy as sp
from scipy.stats import mannwhitneyu, ks_2samp
import numpy as np
import math

def get_u_statistics(x, y):

    u_stat, p_stat = mannwhitneyu(x, y, True, 'two-sided')
    effect_size = 1 - float(2 * u_stat / (len(x)*len(y)))
    return u_stat, p_stat, math.sqrt(effect_size**2)

def get_ks2_statistics(x,y):
    d_stat, p_value = ks_2samp(x,y)
    return d_stat, p_stat

S1 = []
S2 = []


with open(sys.argv[1], 'r') as f1:
    for line in f1:
        S1.append(float(line.strip("\n").split(" ")[0]))

with open(sys.argv[2], 'r') as f2:
    for line in f2:
        S2.append(float(line.strip("\n").split(" ")[0]))



u_stat, p_stat , effect_size = get_u_statistics(np.asarray(S1), np.asarray(S2))
d_stat, v_stat = get_ks2_statistics(np.asarray(S1), np.asarray(S2))
#zscore = math.sqrt(len(S1)*len(S2) / (len(S1)+len(S2)))*d_stat
print u_stat, p_stat, effect_size


