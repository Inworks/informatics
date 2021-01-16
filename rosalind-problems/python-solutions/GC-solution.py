import re
with open('/Users/jamison/Downloads/rosalind_gc-2.txt') as f:
    source_dna = f.read()
print source_dna
## Function that calculates GC content
def contentGC(dna):
    c = float(len(re.findall(r'C', dna)))
    g = float(len(re.findall(r'G', dna)))
    total_dna = float(len(re.findall(r'[A-T]', dna)))
    GC = (c + g) / total_dna
    return GC

tag = re.findall(r'>(\w+_\d+)', source_dna) ## Finds >Rosalind_#### titles

clean = source_dna.replace('\n', '') ## Removes all new line characters
dna = re.findall(r'\d+(\w+)>', clean) ## Isolates all DNA strands

results = [] ## Sets up empty list for function results
for elem in dna: ## Runs above function on all elements in list dna
    fxn = contentGC(elem)
    results.append(fxn) ## Adds values to list

mostGC = max(results) ## Greatest GC content
index = results.index(mostGC) ## Index of mostGC
print('The DNA strand with the greatest GC content is:\n{}\n{}'.format(tag[index], mostGC*100))
