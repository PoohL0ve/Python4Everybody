# **Python4Everybody**
Exercises and understanding from [py4e](https://www.py4e.com/)

### Variables and Expressions

### Iterations
An iteration is a repeated task such as a loop and there are two types **while** and **for**: 
  1. While statement
    * indefinite loops;
    * should have an additional statement so the loop doesn't go on forever;
    * uses boolean expressions;
    * can use _continue_ to skip an iteration and _body_ to exit the entire while   statement. 
    ``` flavor = 0
        while flavor <= 12 :
           flavor = flavor + 1
           if flavor == 4 :
               continue
           if flavor == 12 :
               break
               print(flavor)
        print('Delicious')    ```   

  2. For statement
    * definite loop - iterates through the body a specified number of times;
    * uses the _in_ function to assess through the variable
    * utilizes an iteration variable. 
    ``` burger = ['buns, cheese, patty, lettuce, tomato, sauce']
        for things in burger : 
            print(things)
        print('Time to order') ```
