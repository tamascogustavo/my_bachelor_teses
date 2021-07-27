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

    Obs: no caso pegeui so reads pois são os arquivos onde os reads não alinhados foram removidos
    """
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if ".bam" and "reads" in file and "fastq" not in file:
                files.append(os.path.join(r,file))
    return files

def get_file_m(path):
    """This function creates the path for all your files

    input: is a string with the path to your folder containing all files
    Out: is a list of strings containing the path of all files

    Obs: no caso pegeui so reads pois são os arquivos onde os reads não alinhados foram removidos
    """
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if file.startswith("reads_") and "montagem" in file:
                files.append(os.path.join(r,file))
    return files

def get_file_final(path):
    """This function creates the path for all your files

    input: is a string with the path to your folder containing all files
    Out: is a list of strings containing the path of all files

    Obs: no caso pegeui so reads pois são os arquivos onde os reads não alinhados foram removidos
    """
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if file.startswith("only") and "montagem" in file:
                files.append(os.path.join(r,file))
    return files

def fastq_converter(files):
    for file in files:
        out_name = file.split("/")[-1][0:-12]
        out_name = "{}.fastq".format(out_name)
        if os.path.exists(out_name):
            print("{0} already exists".format(out_name))
        else:
            cmd_bam2fq = "samtools fastq {0} > {1}".format(file, out_name)
            exit_message = subprocess.check_call(cmd_bam2fq,shell = True)
            print("Exit status: {0}".format(exit_message))
            print("{0} was created".format(out_name))

def get_fq(path):
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if "fastq" in file and "combined" not in file:
                files.append(os.path.join(r,file))
    return files

def run_canu(files):
    for file in files:
        out_name = file.split("/")[-1][:-6]
        if os.path.exists(out_name):
            print("{} already exists".format(out_name))
        else:
            cmd_canu = "canu -p {0} -d pantoea_{1} genomeSize=4.8m -pacbio-raw {2}".format(out_name,out_name,file)
            exit_message = subprocess.check_call(cmd_canu, shell = True)
            print("Exit status: {0}". format(exit_message))
            print("{} was created".format(out_name))

def main():
    """Main code of the script"""
    #Get the files
    path_to_bam = "/Users/gustavotamasco/pantoea_contaminants"
    files = get_file_final(path_to_bam)
    #Convert to fastq
    fq_files = fastq_converter(files)
    #Get the fq files
    dirpath = os.getcwd()
    os.chdir(dirpath)
    fq = get_fq(dirpath)
    run_canu(fq)


# main
if __name__ == '__main__':
    main()
