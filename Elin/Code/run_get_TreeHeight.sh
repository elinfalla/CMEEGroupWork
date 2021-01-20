#!/bin/bash
# Author: Ioan ie917@ic.ac.uk #change
# Script: run_get_TreeHeight.sh
# Desc: Script to run the get_TreeHeight.R script with trees.csv as a command line argument
# Arguments: none #change NO ARGUMENTS NEEDED
# Date Dec 2020

Rscript get_TreeHeight.R ../Data/trees.csv

R_FILE=../Results/trees_treeheights.csv # change

if [ -f "$R_FILE" ];
then
    echo "$R_FILE exists."
else
    echo "$R_FILE does not exist.";
    exit 1
fi


python3 get_TreeHeight.py ../Data/trees.csv

PY_FILE=../Results/trees_treeheights_py.csv

if [ -f "$PY_FILE" ];
then
    echo "$PY_FILE exists."
else
    echo "$PY_FILE does not exist.";
    exit 1
fi
