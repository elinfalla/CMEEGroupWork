#!/bin/bash

# Author: Elin Falla - ef16@ic.ac.uk # change ADD NAMES

# Script: run_Vectorize.sh

# Desc: times the R and Python versions of Vectorize1 and Vectorize2

# Arguments: none

# Date: Oct 2020

#chmod +x ./Vectorize1.R
#chmod +x ./Vectorize2.R
echo "------ VECTORIZE1.R OUTPUT ------"
Rscript Vectorize1.R
echo "------ END OF OUTPUT ------"

echo "------ VECTORIZE2.R OUTPUT ------"
Rscript ./Vectorize2.R
echo "------ END OF OUTPUT ------"

echo "------ VECTORIZE1.PY OUTPUT ------"
python3 ./Vectorize1.py
echo "------ END OF OUTPUT ------"

echo "------ VECTORIZE2.PY OUTPUT ------"
python3 ./Vectorize2.py
echo "------ END OF OUTPUT ------"
