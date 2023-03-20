# Calculating pay rate by calling a defined function
# Using 40 as the standard work week hours

hours = input('Hours worked: ')
rate = input('Pay rate: ')
convert_hours = float(hours)
convert_rate = float(rate)

def computepay(convert_hours, convert_rate) :
    if convert_hours <= 40 :
        gross_pay = convert_hours * convert_rate
        return gross_pay 
    elif (convert_hours > 40) :
        added_hours = convert_hours - 40
        added_pay = (convert_rate * 0.5) * added_hours
        gross_pay = (convert_hours * convert_rate) + added_pay
        return gross_pay 
    else :
        print('Please input valid numbers.')
salary = computepay(convert_hours, convert_rate)
print('Pay', salary)

# use a variable to store the function when calling it with print. 

