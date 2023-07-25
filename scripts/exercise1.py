import sys 


def read_fasta(file_name):
    """
    parse a fasta file given as a filepath to tupple of head and sequence and check them
    """
    with open(file_name) as file:
        # read the header as a string and remove EOL
        header = file.readline().strip()
        # checks if the first line starts with '>'
        if not header or not header.startswith('>'):
            raise ValueError("Wrong FASTA file: the name should not be empty and should start with '>'")

        # join to a single string line-separated sequence without EOLs
        sequence = ''.join(x.strip() for x in file)
    # checks if the sequence is not empty
    if not sequence:
        raise ValueError('The sequence should not be empty')
    if '>' in sequence:
        raise ValueError('The FASTA file should contain only one DNA sequence')
        

    # convert the sequence into a set of unique bases
    seq1 = set(sequence)
    # create a set of bases
    seq2 = {'A', 'C', 'G', 'T'}
    # check for unknows symbols
    if seq1 - seq2:
        raise ValueError('Wrong sequence')
    return header, sequence


def gc_percentage(sequence):
    """
    calculate G and C percentage in the sequence, rounded to the second decimal place 
    """
    gc = sequence.count('G') + sequence.count('C')
    return round(gc / len(sequence) * 100, 2)


def count(sequence, subsequence):
    """
    calculate a number of subsequences in the sequence
    """
    return sequence.count(subsequence)

# check if the user run the file and print the results
if __name__ == '__main__':
    header, sequence = read_fasta(sys.argv[1])
    print(header)
    print('The sequence length is', len(sequence))
    print('The GC percentage of the sequence is', gc_percentage(sequence), '%')
    print('The number of times the substring ATAT occurs in the DNA string is', count(sequence, 'ATAT'))
