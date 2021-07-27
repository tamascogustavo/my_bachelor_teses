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
def parse_names(fasta):
    all_names = {}
    for line in fasta:
        if line.startswith(">"):
            label = line.strip().split(":")[0]
            name = line.strip().split(":")[1]
            all_names[label] = name
    return all_names

def parse_prot(file):
    seq_dic = {}
    for line in file:
        if line.startswith(">"):
            label = line.strip()
            seq_dic[label] = ""
        else:
            seq_dic[label] += line.strip()
    return seq_dic

def give_names(names, prot_dic):
    named_prot = {}
    for k,v in names.items():
        if k in prot_dic.keys():
            named_prot[v] = prot_dic[k]
    return named_prot

def write_out(info):
    #opening new file
    out = open("pantoea_rast.faa", "w")
    for k, v in info.items():
        exit_info = (">{0}\n{1}".format(k,v))
        out.write(exit_info)
        out.write("\n")
    out.close()


def main():
    """Main code of the script"""
    with open(argv[1]) as fasta_file:
        names = parse_names(fasta_file)

    with open(argv[2]) as prot_file:
        prot_dic = parse_prot(prot_file)
    named_prot = give_names(names,prot_dic)
    write_out(named_prot)

# main
if __name__ == '__main__':
    main()
