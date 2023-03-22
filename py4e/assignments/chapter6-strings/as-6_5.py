# Finding things in strings using find() and slice []

str = 'X-DSPAM-Confidence: 0.8475'

# Find the portion after the ':' and extract the number as a float



portion = str.find(':')
print(portion)
print(str[18:])
extractednumber = float(str[18+2:])
print(extractednumber)