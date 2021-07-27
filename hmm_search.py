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
            if '.hmm' in file:
                files.append(os.path.join(r,file))
    return files


def run_search(files,db):
    for file in files:
        out_name = file.split("/")[-1][0:-4]
        search_out_name = "{0}.out".format(out_name)
        if os.path.exists(search_out_name):
            print("{0} already exists".format(search_out_name))
        else:
            cmd_hmmsearch = "hmmsearch {0} {1} > {2}.out".format(file, db, out_name)
            exit_message = subprocess.check_call(cmd_hmmsearch, shell=True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))


def main():
    """Main code of the script"""

    #only thing that need to be changed is the location folder
    path = "/Users/gustavotamasco/hmmer_info/biofilm"
    database = "/Users/gustavotamasco/pantoearast/rastout/pantoea_rast.faa"
    files = get_file(path)
    run_search(files, database)




# main
if __name__ == '__main__':
    main()
