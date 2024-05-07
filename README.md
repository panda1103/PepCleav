## PepCleav: A feasible strategy for evaluating the cleavability of peptide presented by MHC class I

## Description
This package contains a script to run PepCleav.
PepCleav assesses terminal cleavability based on the amino acid types at the key sites of C-terminus and N-terminus, 
and then integrates the two terminal scores to determine the cleavability of peptide fragment.

## Usage
```
python pepcleav.py --help
usage: pepcleav.py [-h] --input_file INPUT_FILE 
                   [--output_file OUTPUT_FILE] 
                   [--C_terminus C_TERMINUS] 
                   [--N_terminus N_TERMINUS]

optional arguments:
  -h, --help            show this help message and exit
  --input_file          Input file (*.csv)
  --output_file         Output file (default = ./PepCleav_result.csv)
  --C_terminus          The cleavability of the amino acid at the P1 site of C-terminus.
                        (default = ./C.list)
  --N_terminus          The cleavability of the amino acid at the P2 site of N-terminus.
                        (default = ./N.list)
```
For peptide cleavability prediction, you can:
```
python pepcleav.py --input_file test_input.txt --output_file test_output.txt
```
Input files example: test_input.txt, it must has a header:"Peptides"
```
Peptides
ASILRGGKLDK
SILRGGKLDK
SGGELDKWEK
GELDRWEKI
GKLDSWEKIRLR
KLDKWEKIR
```
Output files example: test_output.txt. it includes six columns:   
Peptides,   #peptide sequence  
C-terminal_P1,   #amino acid at the P1 site of C-Terminus   
N-terminal_P2,   #amino acid at the P2 site of N-Terminus   
C_Cleavability_Level,    
N_Cleavability_Level,    
Peptide_Cleavability_Level,   
Level,    #peptide cleavability level  
Rank,     
```
Peptides,C-terminal_P1,N-terminal_P2,C_Cleavability_Level,N_Cleavability_Level,Peptide_Cleavability_Level,Level,Rank
ASILRGGKLDK,K,S,Medium,Low,Medium_Low,Level 2,2
SILRGGKLDK,K,I,Medium,Low,Medium_Low,Level 2,2
SGGELDKWEK,K,G,Medium,Low,Medium_Low,Level 2,2
GELDRWEKI,I,E,Medium,High,Medium_High,Level 4,4
GKLDSWEKIRLR,R,K,Medium,Low,Medium_Low,Level 2,2
KLDKWEKIR,R,L,Medium,High,Medium_High,Level 4,4
DAWEKIRLRPG,G,A,Low,Medium,Low_Medium,Level 2,2
RWEKIRLRP,P,W,Low,Low,Low_Low,Level 1,1
KIRLRPGGKKK,K,I,Medium,Low,Medium_Low,Level 2,2
```
