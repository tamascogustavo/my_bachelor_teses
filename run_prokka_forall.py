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
            if '.fasta' in file:
                files.append(os.path.join(r,file))
    return files

def run_prokka(files):
    for file in files:
        out_name = file.split("/")[-1][0:-6]
        prokka_out = "prokka_{0}".format(out_name)
        if os.path.exists(prokka_out):
            print("{0} already exists".format(prokka_out))
        else:
            cmd_prokka = "prokka --kingdom Bacteria --outdir prokka_{0} {1}".format(out_name, file)
            exit_message = subprocess.check_call(cmd_prokka, shell=True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))

def main():
    """Main code of the script"""
    # only thing that need to be changed is the location folder
    #path = "/Users/gustavotamasco/pantoea_pangenome/all_genomes2"
    dirpath = os.getcwd()
    os.chdir(dirpath)
    files = get_file(dirpath)
    run_prokka(files)

# main
if __name__ == '__main__':
    main()
