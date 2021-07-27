#!/user/bin/env python3
"""
Author: Gustavo Tamasco
Script to run:

The script takes: 

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
            if '.fasta' and 'ref' in file:
                files.append(os.path.join(r,file))
    return files

def run_mummer(files,bb):
    for file in files:
        out_name = file.split("/")[-1]
        mummer_out = "mummer_{0}".format(out_name)
        if os.path.exists(mummer_out):
            print("{0} already exists".format(mummer_out))
        else:
            cmd_mummer = "nucmer {0} {1}".format(file, bb)
            exit_message = subprocess.check_call(cmd_mummer, shell=True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))


def main():
    """Main code of the script"""
    # only thing that need to be changed is the location folder
    path = "/Users/gustavotamasco/PycharmProjects/tcc"
    bb_file = '/Users/gustavotamasco/PycharmProjects/tcc/33_1.fasta'
    #dirpath = os.getcwd()
    #os.chdir(dirpath)
    files = get_file(path)
    run_mummer(files, bb_file)



# main
if __name__ == '__main__':
    main()
