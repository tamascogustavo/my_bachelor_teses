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

def set_size(seq):
    sized_seq = []
    for k,v in seq.items():
        for i,nt in enumerate(v):
            if i < 50000:
                sized_seq.append(nt)
    return("".join(map(str, sized_seq)))

def write_out(seq,outname):
    #opening new file
    out = open(outname, "w")
    exit_info = (">{0}\n{1}".format(outname,seq))
    out.write(exit_info)
    out.write("\n")
    out.close()

def main():
    """Main code of the script"""
    with open(argv[1]) as file1:
        seq1 = parseseq(file1)
        seq1c= set_size(seq1)
        out_name1 = "agglomerans.fasta"
        write_out(seq1c,out_name1)

    with open(argv[2]) as file2:
        seq2 = parseseq(file2)
        seq2c = set_size(seq2)
        out_name2 = "cypredi.fasta"
        write_out(seq2c,out_name2)



# main
if __name__ == '__main__':
    main()
