#!/user/bin/env python3
"""
Author: Gustavo Tamasco
Script to run:

The script takes: 

Run the code by: ex_p5.py <reference_fasta_file> <related_fasta_file>
"""

# import statements
from sys import argv
import os
import subprocess


# functions and classes
def parse_file(file):
    ''' This function parses the single file of multiple fasta files
    into a dictionary

    '''
    seq_dic = {}
    for line in file:
        if line.startswith(">"):
            label = line.strip().split(">")[1]
            seq_dic[label] = " "
        else:
            seq_dic[label] += line.strip()
    return seq_dic

def get_info(file):
    """ This function can be used to write out small parts of the dict
    like a single sequence

    """
    seqs = []
    for k, v in file.items():
        seqs.append(v)
    print(seqs[4])

def get_file(path):
    """This function creates the path for all your files

    input: is a string with the path to your folder containing all files
    Out: is a list of strings containing the path of all files

    """
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if 'contig' in file:
                files.append(os.path.join(r,file))
    return files

def run_blast(files):
    """Run the program blast"""
    out_names = []
    for item in files:
        out_name = item.split("/")[-1]
        out_names.append(out_name)
    for fi, out in zip(files, out_names):
        cmd_blast = "blastn -db all_ref.fasta -query{0} -out {1}".format(fi,out)
        exit_message = subprocess.check_call(cmd_blast, shell=True)
        print("Exit Status: {0}".format(exit_message))
        print("{0} was created".format(out))


def main():
    """Main code of the script"""
    with open(argv[1]) as file:
        #dic = parse_file(file)
        #get_info(dic)
        path = '/Users/gustavotamasco/PycharmProjects/tcc'
        files = get_file(path)
        new_files =[]
        for f in files:
            nf = "'{0}'".format(f)
            new_files.append(nf)
        run_blast(new_files)



# main
if __name__ == '__main__':
    main()
