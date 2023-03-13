# Calculating pay rate by calling a defined function

hours = input('Hours worked: ')
rate = input('Pay rate: ')
hrs = float(hours)
rt = float(rate)

def computepay(hrs, rt) :
    if hrs <= 40 :
        return hrs * rt 
    else :
        fhrs = hrs - 40
        frt = rt * 0.5 
        ovt = fhrs * frt 
        return (hrs * rt) + ovt 
salary = computepay(hrs, rt)
print('Pay', salary)

# use a variable to store the function when calling it with print. 

# I am unclear why using 0.5 works but not 1.5. 