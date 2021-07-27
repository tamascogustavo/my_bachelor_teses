#!/user/bin/env python3
"""
Author: Gustavo Tamasco
Script to run:

The script takes: 

"""

# import statements
from sys import argv
import os
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
            if '.fasta' in file:
                files.append(os.path.join(r,file))
    return files

def get_msa(path):
    """This function creates the path for all your files

    input: is a string with the path to your folder containing all files
    Out: is a list of strings containing the path of all files

    """
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '_msa' in file:
                files.append(os.path.join(r,file))
    return files

def run_mafft(files):
    for file in files:
        out_name = file.split("/")[-1][0:-6]
        msa_outname = "{}_msa".format(out_name)
        if os.path.exists(msa_outname):
            print("{0} already exists".format(msa_outname))
        else:
            comd_mafft = "mafft --auto {0} > {1}_msa".format(file,out_name)
            exit_message = subprocess.check_call(comd_mafft, shell=True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))

def run_hmmbuild(files):
    for file in files:
        out_name = file.split("/")[-1][0:-4]
        hmm_outname = "{0}.hmm".format(out_name)
        if os.path.exists(hmm_outname):
            print("{0} already exists".format(hmm_outname))
        else:
            cmd_hmm = "hmmbuild {0}.hmm {1}".format(out_name, file)
            exit_message = subprocess.check_call(cmd_hmm, shell=True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))


def main():
    """Main code of the script"""
    #only thing that need to be changed is the location folder
    path = "/Users/gustavotamasco/Downloads/phosphate"
    files = get_file(path)
    run_mafft(files)
    dirpath = os.getcwd()
    os.chdir(dirpath)
    new_files = get_msa(dirpath)
    run_hmmbuild(new_files)



# main
if __name__ == '__main__':
    main()
