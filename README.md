# Batch downsampling
*created by Jes Adams (jadams8)*

## About
Python script for downsampling batches of fastq files according to sample name using the seqtk toolkit.

* This script will downsample the paired reads to a given number in the forward and reverse fastq files for a list of given samples in a text file.
* The samples in the text file must be formatted as a list and sample numbers given in the format `*SAMPLE_NUMBER*` for example: `*ABC012345*`

## Dependencies
This script relies on the seqtk toolkit and has been tested using python 3.5.1

## Usage
This script takes arguments for the number of reads (which should be half the total number of reads required) and the text file that contains the list of samples
Called on the command line in the following format (using python 3): 

`python Downsample_txt.py num_of_reads name_of_text_file.txt`

for example: 

`python Downsample_txt.py 20000000 samples.txt`

If number of reads and name of text file are not included then the script will not run.
Use `-h` for help with positional arguements.
