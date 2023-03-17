# adding try/except to as-3_2

hours = input('How many hours did you work?\n')
rate = input('What is your pay-rate?\n')
convert_hours = float(hours)
convert_rate = float(rate)

if convert_hours <= 40 :
    try :
        gross_salary = convert_hours * convert_rate
    except :
        print('Please enter numeric figures')    
else :
    additional_hours = convert_hours - 40
    extra_pay = (convert_rate * 0.5) * additional_hours 
    gross_salary = convert_hours * convert_rate + extra_pay 
print(gross_salary)    
