import os,sys,string,math

xlinkDistanceFile = sys.argv[1]
threshold=float(sys.argv[2])
percent_cutoff=float(sys.argv[3])
outfile=sys.argv[4]

xdf=open(xlinkDistanceFile,'r')

outf=open(outfile,'w')

for ln in xdf.readlines():
    fields=ln.strip().split()
    
    num_satisfied=0.0
    for i in range(3,len(fields)):
        if float(fields[i])<=threshold:
            num_satisfied+=1.0
    
    percent_satisfied=num_satisfied/float(len(fields)-3)
    if percent_satisfied>=percent_cutoff:
        print >>outf,fields[0],fields[1],fields[2]

    
xdf.close()
outf.close()


