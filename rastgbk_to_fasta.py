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
def parse_fna(fna):
    ''' This function parses fna files

    Input: fna file
    Output: is a dict with id and its sequence
    '''
    seqs = {}
    for line in fna:
        if line.startswith(">"):
            label = line.strip().split(">")[1]
            seqs[label] = " "
        else:
            seqs[label] += line.strip()
    return seqs

def parse_gtf(gtf):
    ''' This function parses the gtf file and extract the ID and function of CDS

    Input: a gff file
    Out: list of tupples with the info
    '''
    information = []
    for line in gtf:
        if line.startswith("tig") and "rna" not in line:
            info = line.strip().split("ID")[1]
            name = info.split(";")[0][1:]
            funct = info.split("Name")[1][1:]
            all = name, funct
            information.append(all)

    return information

def merge_info(fna_d, gtf_lt):
    """This function combine both infos to rename the files
    """
    out_dict = {}
    for id, f in gtf_lt:
        if id in fna_d.keys():
            label = ">{0} = {1}".format(id,f)
            out_dict[label] = fna_d[id]
    return out_dict

def write_out(final_info):
    #opening new file
    out = open("pantoe_rast.fasta", "w")
    for k, v in final_info.items():
        exit_info = ("{0}\n{1}".format(k,v))
        out.write(exit_info)
        out.write("\n")
    out.close()


def main():
    """Main code of the script"""
    with open(argv[1]) as fna_file:
        fna = parse_fna(fna_file)
    with open(argv[2]) as gtf_file:
        gtf = parse_gtf(gtf_file)
    final_info = merge_info(fna, gtf)
    write_out(final_info)

# main
if __name__ == '__main__':
    main()
