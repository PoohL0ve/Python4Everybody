#Program to find gross pay using 1.5 for overtime hours. 

hours = input('How many hours did you work?\n')
rate = input('What is your pay-rate?\n')
convert_hours = float(hours)
convert_rate = float(rate)

if convert_hours > 40 : 
    additional_hours = convert_hours - 40
    extra_pay = additional_hours * (convert_rate * 0.5)
    gross_salary = convert_hours * convert_rate + extra_pay 
else :
    gross_salary = convert_hours * convert_rate 
print('Pay: ', gross_salary)

# remember input values are strings. 