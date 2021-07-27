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
            if '.out' in file:
                files.append(os.path.join(r,file))
    return files
def parse_info(data):
    all_hits = []
    for line in data:
        if line.startswith(">>"):
            hit = line.strip().split(">>")[1]
            all_hits.append(hit)
    return all_hits

def print_info(info):
    for k in info.keys():
        for item in info[k]:
            print("{0}\t{1}".format(k,item))

def main():
    """Main code of the script"""
    dirpath = os.getcwd()
    path = '/Users/gustavotamasco/hmmer_info/iaa/iaa_search'
    files = get_file(path)
    info_dic = {}
    for file in files:
        with open(file) as info:
            name = file.strip().split("/")[-1][0:-4]
            hits = parse_info(info)
            info_dic[name] = hits
    print("Feature\tGenome hit")
    print_info(info_dic)


# main
if __name__ == '__main__':
    main()
