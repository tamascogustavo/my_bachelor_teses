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


def main():
    """Main code of the script"""
    with open(argv[1]) as file:
        count = 0
        for line in file:
            if line.startswith(">"):
                count +=1
        print(count)


# main
if __name__ == '__main__':
    main()
