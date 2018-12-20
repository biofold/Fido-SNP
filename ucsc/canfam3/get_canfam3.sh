#!/bin/bash
# Expected files in this directory 
# - canfam3.2bit
# - canfam3.phyloP4way.bw
# - canfam3.phyloP10way.bw
# from http://snps.biofold.org/Fido-SNP/ucsc/canfam3/

path=`dirname $0`

echo '- Download canfam3.2bit'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam3/canfam3.2bit -O $path/canfam3.2bit
echo '- Download canfam3.phyloP4way.bw'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam3/canfam3.phyloP4way.bw -O $path/canfam3.phyloP4way.bw
echo '- Download canfam3.phyloP10way.bw'
wget http://snps.biofold.org/Fido-SNP/ucsc/canfam3/canfam3.phyloP10way.bw -O $path/canfam3.phyloP10way.bw

