import re
with open('/Users/jamison/Downloads/rosalind_hamm.txt') as f:
    dna = f.read()

strands = re.findall(r'(\w+)\n', dna) ## Separates the two DNA strands

dna1 = list(strands[0]) ## Turns each nucleotide into an element in list
dna2 = list(strands[1])

matches = []
for a, b in zip(dna1, dna2): ## Takes each element and pairs them into a tuple
    if a == b:
        matches.append(a) ## Matched nucleotides added to matches list

## Total nucleotides - # matches = Hamming distance
mismatches = len(strands[0]) - len(matches)
print('{} mismatches exist'.format(mismatches))
