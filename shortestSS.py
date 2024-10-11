#####################################
# Implement your code starting here #
#####################################
# Determine overlap
def overlap(a, b, min_length=1):
    """Return the length of the maximum overlap between the suffix of a and the prefix of b."""
    maximum_overlap = 0
    while True:
        maximum_overlap = a.find(b[:min_length], maximum_overlap)
        if maximum_overlap == -1:
            return 0
        if b.startswith(a[maximum_overlap:]):
            return len(a) - maximum_overlap
        maximum_overlap += 1

def find_shortestSS(data):
    '''
    
    You are given at most 50 DNA strings in a dictionary format, with the sequence id as key and the sequence as value. 
    Your code should return the shortest superstring containing all of the provided strings.
    Refer to the example below.

    input: {"read1" : "AATT",
            "read2" : "TTCC",
            "read3" : "CCGG"} 
    return: "AATTCCGG"

    You can create other functions if needed, but the answer should be returned by this function.
    
    '''
# Input
    strings = list(data.values())

    while len(strings) > 1: 
        maximum_overlap_len = -1
        overlap_a, overlap_b = None, None
        overlap_merged = None

# Compare read pairs
        for i in range(len(strings)):
            for j in range(len(strings)):
                if i != j:
                    a, b = strings[i], strings[j]
                    
                    if a in b: 
                        overlap_a, overlap_b = a, b
                        overlap_merged = b
                        maximum_overlap_len = len(a)
                    elif b in a:
                        overlap_a, overlap_b = a, b
                        overlap_merged = a
                        maximum_overlap_len = len(b)
                    overlap_len = overlap(a, b)
# Merge if necessary
                    if overlap_len > maximum_overlap_len:
                        maximum_overlap_len = overlap_len
                        overlap_a, overlap_b = a, b
                        overlap_merged = a + b[overlap_len:]
        
        if overlap_a is not None and overlap_b is not None:
            strings.remove(overlap_a)
            strings.remove(overlap_b)
            strings.append(overlap_merged)
    
# Return merged superstring
    return strings[0] if strings else ""

#####################################
#   Do not modify below this line   #
#####################################

string = {}
try:
    with open("input", "r") as file:
        l = file.readline().rstrip()
        while l:
            if l.startswith(">"):
                id = l.split(">")[1]
                dna = ''
                while l:
                    l = file.readline().rstrip()
                    if l.startswith(">"): 
                        break
                    dna = dna + l
                string[id] = dna
                
except OSError as err:
    print("Failed to open input: {e}".format(e=err))
  
if len(string) > 1:
    ans = find_shortestSS(string)
    print(ans)
else:
    print('Problem reading input, appears to by empty...')