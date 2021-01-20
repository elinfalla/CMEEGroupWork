#!/bin/bash
# Author: Ioan ie917@ic.ac.uk
# Script: run_get_TreeHeight.sh
# Desc: Script to run the get_TreeHeight.R script with trees.csv as a command line argument
# Arguments: get_TreeHeight.sh trees.csv
# Date Dec 2020

Rscript get_TreeHeight.R ../Data/trees.csv

python3 get_TreeHeight.py ../Data/trees.csv