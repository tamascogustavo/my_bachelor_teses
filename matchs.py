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

def get_file(path):
    """This function creates the path for all your files

    input: is a string with the path to your folder containing all files
    Out: is a list of strings containing the path of all files

    """
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r,file))
    return files

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
    dirpath = '/Users/gustavotamasco/pantoea_aligner/teste'
    files = get_file(dirpath)
    for file in files:
        with open(file) as i:
            out_name = file.split('/')[-1][0:-4]
            value = get_match(i)
            print(out_name, value)



# main
if __name__ == '__main__':
    main()
