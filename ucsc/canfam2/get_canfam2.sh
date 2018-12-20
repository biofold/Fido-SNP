#!/bin/bash
# Expected files in this directory 
# - canfam2.2bit
# - canfam2.phyloP4way.bw
# - canfam2.phyloP10way.bw
# from http://snps.biofold.org/Fido-SNP/ucsc/canfam2/

path=`dirname $0`

echo '- Download canfam2.2bit'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam2/canfam2.2bit -O $path/canfam2.2bit
echo '- Download canfam2.phyloP4way.bw'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam2/canfam2.phyloP4way.bw -O $path/canfam2.phyloP4way.bw
echo '- Download canfam2.phyloP10way.bw'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam2/canfam2.phyloP10way.bw -O $path/canfam2.phyloP10way.bw

