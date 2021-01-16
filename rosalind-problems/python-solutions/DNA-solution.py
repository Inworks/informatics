import re
with open('/Users/jamison/Downloads/rosalind_dna.txt') as f:
    data = f.read()

    a = len(re.findall(r'A', data))
    c = len(re.findall(r'C', data))
    g = len(re.findall(r'G', data))
    t = len(re.findall(r'T', data))

    total = a + c + g + t
    bp = len(re.findall(r'[A-T]', data))

print("The number of adenine molecules is: %d" % a)
print("The number of cytosine molecules is: %d" % c)
print("The number of guanine molecules is: %d" % g)
print("The number of thymine molecules is: %d" % t)

if bp == total:
  print "Results valid."
else:
  print "Results invalid."
