with open('/Users/jamison/Downloads/rosalind_prot.txt') as f:
    mrna = f.read()

def codonSplit(dna):
    return [dna[i:i+3] for i in range(0, len(dna), 3)]

def translation(list, dict):
    return [dict.get(item, item) for item in list]


codonDict = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S',
'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C',
'UGC':'C', 'UGA':'Stop', 'UGG':'W', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q',
'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I',
'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N',
'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A',
'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G',
'GGA':'G', 'GGG':'G'
}

codons = codonSplit(mrna)
print "The codons in this mRNA strand are:"
print codons
amino_acids = translation(codons, codonDict)
print "Which results in the amino acids:"
print(''.join(amino_acids))
print(len(amino_acids))
