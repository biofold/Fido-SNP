#!/usr/bin/python
import sys, tempfile
from commands import getstatusoutput
dir_ucsc='/export/emidio/program/PhD-SNPg/ucsc'


def get_vcf_sequences(vcf_file,ucsc_exe,ucsc_dbs,win=2,dbname='hg19.2bit',prog='twoBitToFa'):
	tmpfile=tempfile.mktemp()
	db_file=ucsc_dbs+'/'+dbname
	cmd='zcat -f '+vcf_file+' | grep -v "^#" | awk -F "\\t"  \'{print "chr"$1"\\t"$2-'+str(win)+\
			'"\\t"$2+'+str(win+1)+'"\\t"$1"|"$2"|"$4"|"$5} \' > '+tmpfile 
        out=getstatusoutput(cmd)
        if out[0]!=0:
                print >> sys.stderr,'ERROR: Sequence fetch -', out[1]
                sys.exit(1)
	cmd=ucsc_exe+'/'+prog+' '+db_file+' stdout -bed='+tmpfile+\
		' | grep -v "^>" | awk \'{print toupper($1)}\' > '+tmpfile+'.seq'
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print >> sys.stderr,'ERROR: Sequence fetch -', out[1]
		sys.exit(1)
	return tmpfile



def get_conservation(ichr,start,end,ucsc_exe,ucsc_dbs,dbname='hg19.100way.phyloP100way.bw',prog='bigWigToBedGraph'):
	vcons=[]
	db_file=ucsc_dbs+'/'+dbname        
	cmd=ucsc_exe+'/'+prog+' '+db_file+' stdout -chrom='+ichr+' -start='+str(start)+' -end='+str(end)
	out=getstatusoutput(cmd)
	if out[0]!=0:
		print >> sys.stderr,'ERROR: Conservation fetch -', out[1]	
		sys.exit(1)
	else:
		d={}
		lines=out[1].split('\n')
		for line in lines:
			v=line.split()
			if len(v)<4: continue
			val=float(v[3])
			s=int(v[1])
			e=int(v[2])
			for i in range(s,e):
				d[i]=val
		for i in range(start,end):
			vcons.append(d.get(i,0.0))
	return vcons


def get_file_cons(filename,fileout,ucsc_exe,ucsc_dbs,dbname='hg19.100way.phyloP100way.bw',prog='bigWigToBedGraph'):
	fi=open(filename)
	fo=open(fileout,'w')
	for line in fi:
		v=line.rstrip().split()
		vcons=get_conservation(v[0],int(v[1]),int(v[2]),ucsc_exe,ucsc_dbs,dbname,prog)
		fo.write('\t'.join([str(i) for i in vcons])+'\n')
	fo.close()
	return fileout


if __name__ == '__main__':
	vcf_file=sys.argv[1]
	tmpfile=get_vcf_sequences(vcf_file,dir_ucsc+'/exe',dir_ucsc+'/hg19')
	fileout=get_file_cons(tmpfile,tmpfile+'.prof',dir_ucsc+'/exe',dir_ucsc+'/hg19')
	print fileout



