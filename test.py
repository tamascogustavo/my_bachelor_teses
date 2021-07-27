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

def get_match(file):
    match = []
    for line in file:
        if 'NZ' not in line:
            nm = line.split()[-1]
            match.append(nm)
    final_value = sum(map(int,match))
    return(final_value)

def main():
    """Main code of the script"""
    with open(argv[1]) as file:
        name = 'test'
        value = get_match(file)
        print(name,value)


# main
if __name__ == '__main__':
    main()
