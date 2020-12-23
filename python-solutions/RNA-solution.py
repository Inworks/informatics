import re
with open('/Users/jamison/Downloads/rosalind_rna.txt') as f:
    data = f.read()

print re.sub(r'T', r'U', data)

## Or alternatively: print(data.replace('T', 'U'))
