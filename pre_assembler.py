#!/user/bin/env python3
"""
Author: Gustavo Tamasco
Script to run:

The script takes:
The script takes genome fasta files or files containing the contigs of one assemble and:

1. Mapear usando minimap2
2. Converter os arquivos .sam em sorted bam
3. Indexar os arquivos de .bam
4. Visualizar o número de reads fora do alinhamento
5. Criar um arquivo .bam contendo somente os reads alinhados
"""

# import statements
from sys import argv
import os.path
import subprocess


# functions and classes

def get_genomes(path):
    files = []
    for r,d,f in os.walk(path):
        for folder in d:
            if "pantoea_only" or "pantoea_reads" and "_montagem" in folder and "montagem." not in folder:
                for a,s,d in os.walk(folder):
                    for file in d:
                        if ".contigs.fasta" in file and "fasta.fai" not in file:
                            files.append(os.path.join(a,file))
    return(files)


def run_minmap(files, ref):
    names = []
    for file in files:
        out_name = file.split("/")[-1][:-14]
        out_name = "{}_final_align.sam".format(out_name)
        names.append(out_name)
        if os.path.exists(out_name):
            print("{} already exists". format(out_name))
        else:
            cmd_minmap = "~/minimap2/minimap2 -a  {0} {1} > {2}".format(file, ref, out_name)
            exit_message = subprocess.check_call(cmd_minmap, shell= True)
            print("Exit status: {0}". format(exit_message))
            print("{} was created".format(out_name))
    return(names)

def sort_sam(files):
    names = []
    for file in files:
        out_name = file.split(".")[0]
        out_name = "{}_sorted.bam".format(out_name)
        names.append(out_name)
        if os.path.exists(out_name):
            print("{} already exists".format(out_name))
        else:
            cmd_sort_sam = "samtools sort {} > {}".format(file, out_name)
            exit_message = subprocess.check_call(cmd_sort_sam, shell= True)
            print("Exit status: {}".format(exit_message))
            print("{} was created".format(out_name))
    return names

def index_bam(files):
    names = []
    for file in files:
        out_name = "{}.bai".format(file)
        names.append(out_name)
        if os.path.exists(out_name):
            print("{} already exists".format(out_name))
        else:
            cmd_ind_bam = "samtools index -b {}".format(file)
            exit_message = subprocess.check_call(cmd_ind_bam, shell=True)
            print("Exit status: {}".format(exit_message))
            print("{} was created".format(out_name))
    return names

def check_reads(files):
    for file in files:
        cmd_check = "samtools view -f4 -c {}".format(file)
        all_reads = "samtools view -c {}".format(file)
        exit_message1 = subprocess.check_call(cmd_check, shell= True)
        out_1 = subprocess.check_output(cmd_check, shell = True)
        exit_message2 = subprocess.check_call(all_reads, shell= True)
        out_2 = subprocess.check_output(all_reads, shell=True)
        print("{} has {} reads not aligned, the total amount of reads was {}.".format(file,out_1.strip(),out_2.strip()))

def run_parser(files):
    names = []
    for file in files:
        out_name = file.split("_")[0:4]
        out_name = "only_match_{}.bam".format("_".join(map(str,out_name)))
        names.append(out_name)
        if os.path.exists(out_name):
            print("{} already exists".format(out_name))
        else:
            cmd_get_reads = "samtools view -F 0x04 -b  {} > {}".format(file, out_name)
            exit_message = subprocess.check_call(cmd_get_reads, shell= True)
            print("Exit status: {}".format(exit_message))
            print("{} was created".format(out_name))
    return names


def main():
    """Main code of the script"""
    ref_path = "/Users/gustavotamasco/pantoea_contaminants/combined.fasta"
    path = os.getcwd()
    os.chdir(path)
    files = get_genomes(path)
    print(files)
    mapped = run_minmap(files, ref_path)
    sorted_bam = sort_sam(mapped)
    indexed_bam = index_bam(sorted_bam)
    reads_not_aligned = check_reads(sorted_bam)
    reads_aligned = run_parser(sorted_bam)




# main
if __name__ == '__main__':
    main()
