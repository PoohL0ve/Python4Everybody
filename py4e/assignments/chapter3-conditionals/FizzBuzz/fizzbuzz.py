# simple fizzbuzz program
# if number is divisible by 3 print fizz
# if number is divisble by 5 print buzz
# if number is divisible by both 3 and 5 print fizzbuzz

number = int(input('Please enter a number'))

if number % 3 == 0 and number % 5 ==0 :
    print('FizzBuzz')
elif number % 3 == 0 :
    print('Fizz')
elif number % 5 == 0 :
    print('Fuzz')
else :
    print('Not a valid checker')     