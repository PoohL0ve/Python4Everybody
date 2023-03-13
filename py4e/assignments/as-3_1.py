# Trying out what I have learnt, thus far.

#Program to find gross pay using 1.5 for overtime hours. 

hours = input('Enter Worked Hours :')
rate = input('Pay Rate :')
chrs = float(hours)
crat = float(rate)

if hours > '40' :
    ovt = chrs - 40
    orat = crat * 0.5 
    esal = ovt * orat 
    sal = (chrs * crat) + esal 
else :
    sal = chrs * crat
print('Pay:',sal)

# remember input values are strings. 