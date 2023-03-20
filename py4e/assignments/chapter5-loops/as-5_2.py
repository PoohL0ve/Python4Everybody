# Using a while statement with try and except: write a program that prompts a user for numbers
# enter numbers 2, 4, 7 and 10, as well as string: bob and done
# use 10 for the largest number and 2 for the smallest
# if done is entered end the program. 

Largest = None
Smallest = None #None has no value or type

while True :
    text = input('Enter a number : ')
    if text == 'done' :
        break
    try:
        num = int(text)
        if Largest is None or num > Largest :
           Largest = num
        if Smallest is None or  num < Smallest :
            Smallest = num     
    except:
        print('Invalid input')       
print('Maximum is', Largest)
print('Minimum is', Smallest)

# the break was done outside the try and except statement using the original variable text

    
    
       