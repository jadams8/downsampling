"""
This script will downsample the paired reads to a given number in the forward and reverse fastq files for a list of given samples in a text file. 
The samples in the text file must be formatted as a list and sample numbers given in the format *SAMPLE_NUMBER* for example: *EX0123456*
This script takes arguments for the number of reads (which should be half the total number of reads required) and the text file that contains the list of samples
Called on the command line in the following format (using python 3): python downsample.py num_of_reads name_of_text_file.txt 
for example: python downsample.py 20000000 samples.txt 
If number of reads and name of text file are not included then the script will not run.
Use -h for help with positional arguements
vars is where filepaths will be held.
"""

import os, fnmatch, subprocess, gzip, argparse
import vars

#define command line positional arguments and help messages 

parser = argparse.ArgumentParser(description='This is a python3 script to downsample a list of samples given in a list in a text file. Please include number of reads and name of text file in command')
parser.add_argument("reads", help='enter half the total number of reads you wish to downsample each sample to')
parser.add_argument("samples", help='enter the name of the text file containing the list of samples to downsample')
args = parser.parse_args()


#make a list of samples to downsample using the file given as an argument

samples = []
input_file = args.samples
file = open(input_file, 'r')
samples = file.read().splitlines()
file.close()


#check all the samples have been read in correctly

#print (samples)


#specify the directories for the program to look in to save time

paths = vars.paths


#loop through the samples, looking in each specified path to find .gz files that contain the sample number.
#create a list of all the files found for each sample- there should be a forward and reverse fastq for each sample.

result = []
for sample in samples:
        for path in paths:
#                print ('searching in '+path+' for '+sample)
                for root, dirs, files in os.walk(path):
                        for name in files:
                                if fnmatch.fnmatch(name, sample) and name.lower().endswith('gz'):
#                                        print (sample+' file found')
                                        result.append(os.path.join(root, name))


#create a variable containing the directory to the seqtk executable

seqtk_dir = vars.seqtk


#set a variable containing the number of reads to downsample to and a variable for naming the output file

num_of_reads = args.reads
output_reads = num_of_reads[:2]+'M'


#for each file in results, loop through and use subprocess to downsample each file using seqtk and zip using gzip

for file in result:
	out_file = file.split('/')[-1].split('.')[0]+'_'+output_reads+'.fastq.gz'
	with gzip.open(out_file, 'wb') as f:
		seqtk = [seqtk_dir, 'sample', '-s100', file, num_of_reads]
		cmd1 = subprocess.Popen(seqtk, stdout=subprocess.PIPE)
		zip = ['gzip']
		cmd2 = subprocess.Popen(zip, stdin=cmd1.stdout, stdout=f) 
		cmd2.communicate()

#print file complete at the end of each file to know when each one is complete

#		print ('file complete')
