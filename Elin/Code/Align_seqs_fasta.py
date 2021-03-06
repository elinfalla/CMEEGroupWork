#!/usr/bin/env python3

"""Finds the best alignment of two DNA sequences (ie. the alignment with the most matched bases) from two inputted
FASTA files. Writes the alignment and the number of matches to a file called Alignment_output.txt."""

__appname__ = "Align_seqs.py"
__author__ = "Elin Falla, ef16@ic.ac.uk"
__version__ = "0.0.1"

# Imports #
import sys


# Functions #
def fasta_to_string(fastafile):
    """Converts a fasta file to a string (removes first line and new line characters)"""

    # Read fasta file into a string
    sequence = fastafile.read()

    # Remove first line
    sequence = sequence.split("\n", 1)[1]  # split at \n, maxsplit = 1, then selects second element (ie. sequence)


    # Remove newline characters if present
    if "\n" in sequence:
        sequence = sequence.replace("\n", "")

    return sequence


def string_swap(seq1, seq2):
    """Assign the longer sequence to s1, and the shorter to s2.
    Calculate l1 and l2: l1 is length of the longer sequence, l2 that of the shorter."""
    l1 = len(seq1)
    l2 = len(seq2)
    if l1 >= l2:  # If l1 is already longer than l2, no need to swap strings
        s1 = seq1
        s2 = seq2
    else:  # If l2 is longer than l1, swap the strings and the lengths
        s1 = seq2
        s2 = seq1
        l1, l2 = l2, l1 # swaps the two lengths
    return s1, s2, l1, l2


def calculate_score(s1, s2, l1, l2, startpoint):
    """Calculates a score by returning the number of matches starting
    from arbitrary start point in the sequence (chosen by user)"""
    matched = ""  # to hold string displaying alignments
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]:  # if the bases match
                matched = matched + "*"  # * indicates a match
                score = score + 1
            else:
                matched = matched + "-"  # - indicates no match

    # Formatted output
    # print("." * startpoint + matched)  # prints '." times whatever number startpoint is set to, then the matched string
    # print("." * startpoint + s2)
    # print(s1)
    # print(score)
    # print(" ")

    return score, matched


def find_best_align(s1, s2, l1, l2):
    """Finds the alignment of two sequences that gives the best match (highest score)"""

    my_best_align = None
    my_best_score = -1
    my_best_match = None

    for i in range(l1):  # Note that you just take the last alignment with the highest score
        z, matched = calculate_score(s1, s2, l1, l2, i)
        if z > my_best_score:
            my_best_align = "." * i + s2  # prints number of '.' to get to startpoint (which is i here)
            my_best_score = z
            my_best_match = "." * i + matched

    # Formatted output
    print(my_best_match)
    print(my_best_align)
    print(s1)
    print("Best score:", my_best_score)

    return my_best_align, my_best_score, my_best_match


def main(argv):
    """Main entry point of the program: reads input file, calculates the best match, and writes it to output file."""

    # If two files not inputted on the command line
    if len(sys.argv) != 3:

        if len(sys.argv) == 2:
            print("Not enough files. Please use 2 fasta files as arguments.")
            return 1
            # TODO check for > to see if multiple sequences in one file. if so, split it??

        elif len(sys.argv) == 1:  # if no arguments given, use default files
            print("No files given. Using default fasta files...")
            fastafile1 = open("../CMEECourseWork/Week2/Data/407228326.fasta", "r")
            fastafile2 = open("../CMEECourseWork/Week2/Data/407228412.fasta", "r")


        else:  # else if more than 3
            print("Too many files. Please use 2 fasta files as arguments.")
            return 2

    else:  # if 2 input files given
        fastafile1 = open(sys.argv[1], "r")
        fastafile2 = open(sys.argv[2], "r")

    seq1 = fasta_to_string(fastafile1)
    seq2 = fasta_to_string(fastafile2)



    # Open the csv file with the DNA sequences
    # sequences = open("../Data/Sequences.csv", "r")

    # Split the csv file by lines and assign the 2 sequences to variables
    # seqs = sequences.read().splitlines()
    # seq1 = seqs[0]
    # seq2 = seqs[1]

    # Run string_swap to find longer sequence
    s1, s2, l1, l2 = string_swap(seq1, seq2)

    # Run find_best_align to find best alignment of sequences
    my_best_align, my_best_score, my_best_match = find_best_align(s1, s2, l1, l2)

    # Write result to an output file called 'Alignment_output.txt'
    output_file = open("../Results/Alignment_output.txt", "w+")
    output_file.write("%s\n%s\n%s\nBest score: %s\n" % (my_best_match, my_best_align, s1, my_best_score))

    # Close the input and output files
    fastafile1.close()
    fastafile2.close()
    output_file.close()

    return 0


if __name__ == "__main__":
    """Makes sure the 'main' function is called from the command line."""
    status = main(sys.argv)
    sys.exit(status)

# TODO FOR GROUP EXERCISE
# function that turns fasta input into string
# function that takes in two dna seqs and outputs (my_best_align, s1, my_best_score)
# main that reads files and outputs resulting file
# Have error message for if 0 or 1 files given, if 0 use default
