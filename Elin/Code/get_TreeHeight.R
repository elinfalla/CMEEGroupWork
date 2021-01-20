#!/usr/bin/env R

# This function calculates heights of trees given distance of each tree
# from its base and angle to its top, using the trigonometric formula
# 
# height = distance * tan(radians)
#
# ARGUMENTS
# degrees: The angle of elevation of tree
# distance: The distance from base of tree (e.g. meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

# Loading data from command line input

args <- commandArgs(trailingOnly = TRUE)

string <- args[1]
# Remove relative path
string <- gsub(".*/","",string)
# Remove file extension
string <- tools::file_path_sans_ext(string)


tree_data <- read.csv(args[1])

# Function

TreeHeight <- function(degrees, distance) {
    radians <- degrees * pi / 180
    height <- distance * tan(radians)
    
    return(height)
}

#change: added t to height - WHY IS THIS HERE?
print(paste("The height of a tree with an angle of 37 degrees at distance 40m is", as.character(TreeHeight(37,40))))

# Assigning the output of the function to a column

tree_data$Tree.Height.m <- TreeHeight(tree_data$Angle.degrees, tree_data$Distance.m)

# Creating a csv output

write.csv(tree_data, paste("../Results/", string, "_treeheights.csv", sep = ""), row.names = FALSE) # change: _treeheights

# Message to state complete

print("get_Treeheight.R complete") # change