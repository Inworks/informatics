with open('/Users/jamison/Downloads/rosalind_revc.txt') as f:
    dna = f.read()

# This function creates an empty string and reverses the given DNA strand
def reverse(text):
    dnaRev = ""
    for letter in text:
        dnaRev = letter + dnaRev
    return dnaRev

# This function utilizes a dictionary to replace complementary bases
def replace_all(text, dict):
    for k, v in dict.iteritems():
        text = text.replace(k, v)
    return text

# This dictionary is used to encode original bases into numbers.
# If one were to just replace bases straight away, a key:value comparison
# would overwrite bases that were already changed from the replace_all function.
encodeDict = {
'A':'1', 'C':'2',
'G':'3', 'T':'4'
}
# This dictionary is used to decode the encoded DNA strand
decodeDict = {
'1':'T', '2':'G',
'3':'C', '4':'A'
}

print dna
reversed_dna = (reverse(dna)) # Reverses DNA strand
print reversed_dna
encoded_dna = replace_all(reversed_dna, encodeDict) # Encodes DNA strand
print encoded_dna
decoded_dna = replace_all(encoded_dna, decodeDict) # Decodes DNA strand
print decoded_dna
