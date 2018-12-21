# Fido-SNP


INTRODUCTION
      
      Emidio Capriotti, 2018.
      Scripts are licensed under the Creative Commons by NC-SA license.

      Fido-SNP is a program for the annotation of single nucleotide variants in dog genome.


INSTALLATION

      Minimum requirements:
      wget, curl, zcat, scikit-learn.

      Run:
        python setup.py install arch_type

      For Linux 64bit architecture there are two compiled versions:
        - linux.x86_64

      Installation time depends on the network speed.
      About 35G of UCSC like files need to be downloaded.

      Test:
        python setup.py test	



MANUAL INSTALLATION

      1) Download Fido-SNP script from github
        - git clone https://github.com/biofold/Fido-SNP

      2) Required python library: scikit-learn
        - git://github.com/scikit-learn/scikit-learn

      3) Required UCSC tools and data:
        - bigWigToBedGraph and twoBitToFa from
          http://hgdownload.cse.ucsc.edu/admin/exe
          in ucsc/exe directory

        - For canfam2 based predictions:
          canfam2.2bit: http://snps.biofold.org/Fido-SNP/ucsc/canfam2/canfam2.2bit
          canfam2.phyloP4way.bw http://snps.biofold.org/ucsc/canfam2/canfam2.phyloP4way.bw
          canfam2.phyloP10way.bw http://snps.biofold.org/ucsc/canfam2/canfam2.phyloP10way.bw

        - For canfam3 based predictions:
          canfam3.2bit: http://snps.biofold.org/Fido-SNP/ucsc/canfam3/canfam3.2bit
          canfam3.phyloP4way.bw http://snps.biofold.org/ucsc/canfam3/canfam3.phyloP4way.bw
          canfam3.phyloP10way.bw http://snps.biofold.org/ucsc/canfam3/canfam3.phyloP10way.bw


HOW TO RUN
		
      Fido-SNP can take in input a single variation or a file containing multiple single nucleotide variants.

      - For single variants use the option -c:
        python fido_variants.py chr1,15189413,C,G -g canfam3 -c

      - For input file the input can be either: 
	
        plain tab separated file with 4 columns: chr, position, ref, alt
        python fido_variants.py test/test_canfam3.tsv -g canfam3
       
        vcf file with in the firt 5 columns: chr, position, rsid, ref, alt  
        python fido_variants.py test/test_canfam3.tsv.gz --vcf -g canfam3


OUTPUT

      Fido-SNP returns in output a probabilistic score between 0 and 1. If the score is >0.5 the variants
      is predicted as disease related. The probability is added as an extra column to the input file. 
      An example of output is reported below.

        1       15189413        C       G       Yes     Pathogenic    0.515   0.075  -0.027   0.317
        5       34700967        T       A       Yes     Benign        0.145   0.242   0.766   0.678
        9       54071528        T       C       Yes     Benign        0.327   0.246  -0.402   0.260
