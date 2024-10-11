def reverse_complement(DNA):
    '''
    Returns the DNA reverse complement.
    '''
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(DNA))

def buildDeBruijn(input):
    '''
    You will be given a set S of up to 1000 DNA strings (repeats may occur) of equal length.
    You are expected to return the adjency list (a two-column matrix that represents the edges
    of a graph) that corresponds to the completed de Bruijn graph. 
    '''
    
    adjacency_list = {}

    def edge_function(kmer):
        '''
        Function that can help add an edge to the adjacency list.
        '''
        prefix = kmer[:-1] 
        suffix = kmer[1:] 
        if prefix not in adjacency_list:
            adjacency_list[prefix] = set()
        adjacency_list[prefix].add(suffix)

# Create the corresponding adjacency list for the k-mers and reverse complements
    for kmer in input:
        edge_function(kmer)
        edge_function(reverse_complement(kmer)) 

# Ensure the adjacency list is in the right format
    results = []
    for prefix, suffixes in adjacency_list.items():
        for suffix in sorted(suffixes):
            results.append(f"({prefix}, {suffix})")
    
    return results

#####################################
#   Do not modify below this line   #
#####################################

input = []
try:
    with open('input', 'r') as file:
        l = file.readline().rstrip()
        while l:
            input.append(l)
            l = file.readline().rstrip()
                
except OSError as err:
    print("Failed to open input: {e}".format(e=err))

if len(input) > 0:
    ans = buildDeBruijn(input)
    for a in ans:
        print(a)
else:
    print('Problem reading the input, appears to be empty...')