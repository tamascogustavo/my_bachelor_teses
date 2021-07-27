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
def parse(file):
    for i, line in enumerate(file):
        if i>0 and "rna" not in line:
            description = line.strip().split(";")[1][5:]
            name = line.strip().split()[8][3:]
            final_name = name.split(";")[0]
            print("{0}\t-\t{1}".format(final_name,description))


def main():
    """Main code of the script"""
    with open(argv[1]) as file:
        parse(file)

# main
if __name__ == '__main__':
    main()
