#!/user/bin/env python3
"""
Author: Gustavo Tamasco
Script to run:

The script takes: 

Run the code by: ex_p5.py <reference_fasta_file> <related_fasta_file>
"""

# import statements
from sys import argv
import os.path
import subprocess


# functions and classes

def parseseq(file):
    seqs = {}
    for line in file:
        if line.startswith(">"):
            label = line.strip()
            seqs[label] = ""
        else:
            seqs[label] += line.strip()
    return (seqs)

def main():
    """Main code of the script"""
    with open(argv[1]) as file1:
        seq1 = parseseq(file1)
        for k,v in seq1.items():
            print(k, len(v))




# main
if __name__ == '__main__':
    main()
