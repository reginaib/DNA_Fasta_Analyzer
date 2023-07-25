# Exercise 1

## Introduction
This Python script takes the location of a FASTA file as an argument, parses the file, and outputs the sequence name, its length, GC percentage, and the number of unique (non-overlapping) "ATAT" subsequence occurrences. 
The script reads a DNA sequence from a FASTA file, and joins it into a single string line, which is used for the calculations. The results are then printed on the screen.

## Requirements for an input file 
The FASTA file should contain a header as its first line and only one DNA sequence written using upper case letters. 

## How to run the script

To run the script, make sure you have Python 3.6 installed on your system. 
The script can be run by invoking it from the command line with the path to a FASTA file as an argument:

```
python exercise1.py path/to/the/fasta/file
```
Replace path/to/the/fasta/file with the path to the FASTA file. Example:   

```
python exercise1.py /lustre1/project/stg_00079/teaching/data/keratin.fasta
```

## Output of the final script run 

This is an example of the output of the script:

```
>Keratin
The sequence length is 1190
The GC percentage of the sequence is 57.73 %
The number of times the substring ATAT occurs in the DNA string is 2
```

## Input and output of the batch job on the VSC
The script can be run as a batch job on the VSC using ```sbatch``` command. The ```exercise1.slrm``` file provides details on the scheduling requirements of the job. A run was submitted to the cluster using a command:
```
sbatch exercise1.slrm
```
The output of the job is saved in the ```exercise1.out``` file and looks as follows:
```
SLURM_CLUSTER_NAME: wice
SLURM_JOB_PARTITION: batch
SLURM_NNODES: 1
SLURM_NODELIST: s28c11n4
SLURM_JOB_CPUS_PER_NODE: 1
Date: Sat Mar 11 19:19:05 CET 2023
Walltime: 00-00:04:00
========================================================================
Sat Mar 11 19:19:05 CET 2023
>Keratin
The sequence length is 1190
The GC percentage of the sequence is 57.73 %
The number of times the substring ATAT occurs in the DNA string is 2
Sat Mar 11 19:19:06 CET 2023
```

## How to test the script
### Testing the script using a bash script
To test the script, simple input files with known outcomes were created:   
```test1.fasta``` contains only 'G' and 'C' in the sequence,  
```test2.fasta``` has 'AT' fragment divided into two lines,  
```test3.fasta``` contains a random sequence,    
```test4.fasta``` contains two 'ATAT' fragments,   
```test5.fasta``` is a file with unknown characters in the sequence,   
```test6.fasta``` contains only a header, but no sequence,   
```test7.fasta``` contains only a sequence, but no header,   
```test8.fasta``` contains two DNA sequences.      

The ```test.sh``` script contains expected outputs of the test input files and commands to run them. The ```test.sh``` file can be executed and saved in ```test_output.txt``` as follows:
```
bash test.sh > test_output.txt 2>&1
```
#### Output of test runs
The output of the test runs is saved in ```test_output.txt``` file:
```
Expected output for test1 is:  
>test1
The sequence length is 8
The GC percentage of the sequence is 100.0 %
The number of times the substring ATAT occurs in the DNA string is 0

>test1
The sequence length is 8
The GC percentage of the sequence is 100.0 %
The number of times the substring ATAT occurs in the DNA string is 0

Expected output for test2 is: 
>test2
The sequence length is 24
The GC percentage of the sequence is 0.0 %
The number of times the substring ATAT occurs in the DNA string is 2

>test2
The sequence length is 24
The GC percentage of the sequence is 0.0 %
The number of times the substring ATAT occurs in the DNA string is 2

Expected output for test3 is: 
>test3
The sequence length is 24
The GC percentage of the sequence is 37.5 %
The number of times the substring ATAT occurs in the DNA string is 1

>test3
The sequence length is 24
The GC percentage of the sequence is 37.5 %
The number of times the substring ATAT occurs in the DNA string is 1

Expected output for test4 is: 
>test4 
The sequence length is 8
The GC percentage of the sequence is 0.0 %
The number of times the substring ATAT occurs in the DNA string is 2 

>test4
The sequence length is 8
The GC percentage of the sequence is 0.0 %
The number of times the substring ATAT occurs in the DNA string is 2

Expected output for test5 is: 
ValueError: Wrong sequence

Traceback (most recent call last):
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 47, in <module>
    header, sequence = read_fasta(sys.argv[1])
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 26, in read_fasta
    raise ValueError('Wrong sequence')
ValueError: Wrong sequence

Expected output for test6 is: 
ValueError: The sequence should not be empty

Traceback (most recent call last):
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 47, in <module>
    header, sequence = read_fasta(sys.argv[1])
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 19, in read_fasta
    raise ValueError('The sequence should not be empty')
ValueError: The sequence should not be empty

Expected output for test7 is: 
ValueError: Wrong FASTA file: the name should not be empty and should start with '>'

Traceback (most recent call last):
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 47, in <module>
    header, sequence = read_fasta(sys.argv[1])
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 13, in read_fasta
    raise ValueError("Wrong FASTA file: the name should not be empty and should start with '>'")
ValueError: Wrong FASTA file: the name should not be empty and should start with '>'

Expected output for test8 is: 
ValueError: The FASTA file should contain only one DNA sequence

Traceback (most recent call last):
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 50, in <module>
    header, sequence = read_fasta(sys.argv[1])
  File "/vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova/exercise1.py", line 21, in read_fasta
    raise ValueError('The FASTA file should contain only one DNA sequence')
ValueError: The FASTA file should contain only one DNA sequence
```

### Testing the script using pytest
Testing of the script can be also performed using ```test.py```. This script uses ```assert``` statements to test the functionality of the read_fasta(), gc_percentage(), and count() functions on various inputs and ```with pytest.raises()``` to catch the exceptions. To test, make sure that pytest is installed and run the ```test.py``` file:

```
pytest test.py
```
All tests should be passed. To invoke the pytest and save the output in the ```test_output.log``` file:
```
pytest test.py > pytest_output.log
```
#### Output of test runs
The output of the test runs is saved in ```pytest_output.log``` file:
```
============================= test session starts ==============================
platform linux -- Python 3.10.9, pytest-7.2.2, pluggy-1.0.0
rootdir: /vsc-hard-mounts/leuven-data/350/vsc35081/exercise1_r0926499_ReginaIbragimova
collected 4 items

test.py ....                                                             [100%]

============================== 4 passed in 0.04s ===============================
```

## Dependencies
This script requires the following dependencies:  
Python 3.6  
Pytest  
