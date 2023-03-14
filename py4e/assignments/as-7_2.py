# Look for certain lines in a file
# Count the lines and extract the floating point values
# Get the average printed as Average spam confidence:

unitlog = input('Enter file here :')
searching = open(unitlog)

glasses = 0
full = 0

for line in searching :
    if not line.startswith('X-DSPAM-Confidence: ') :
        continue
    if line.startswith('X-DSPAM-Confidence: ') :
        glasses = float(glasses) + 1 
        fish = line.find('0')
        caughtit = float(line[fish: ])
        full = caughtit + full
average = full / glasses 
print('Average spam confidence:', average)        
        