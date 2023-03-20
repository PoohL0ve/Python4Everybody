# Let a user input any amount of numbers 
# Once done is typed by the user display the total, count and average

count = 0
total = 0
average = 0
while True :
    user_number = input('Enter a number:\n When you are tired enter done')
    try :
        convert_number = float(user_number)
        for figure in convert_number :
            count = count + 1
            total = total + figure 
            average = total / count
    except :
        print("Please enter a valid number") 
        continue  
    if convert_number == 'done' :
        break 
print("Total Attempts: ", count)
print("Sum of number entered: ", total)
print("The average number entered: ", average)