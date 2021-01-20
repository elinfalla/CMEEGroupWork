#!/usr/bin/env py

import csv
import numpy as np
import pandas as pd
import re
import sys

# Loading data from command line input

string = sys.argv[1]

# Remove relative path
string = re.sub(r'^.*/', '', string)
# Remove file extension
string = string.split(".")[0]

#tree_data = open(argv[1], 'r')
df = pd.read_csv("../Data/trees.csv")

# Function

def TreeHeight(degrees, distance):
    radians = np.radians(degrees)
    height = distance * np.tan(radians)
    return height

example = TreeHeight(37, 40)

print(f"The heigh of a tree with an angle of 37 degrees at distance 40m is {example}")

# Assigning the output of the function to a column

df["Tree.Height.m"] = TreeHeight(df["Angle.degrees"], df["Distance.m"]) #### Not working

# Creating a csv output

df.to_csv(f"../Results/{string}.csv", index = False)

# Message to state complete

print("Done")