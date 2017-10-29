# Application for Calculator

from Calculator import Calculator

calculator = Calculator()

numbers = calculator.number_input()

if len(numbers) == 1:# when input is 1 number
    print calculator.x_function(numbers[0])   #run function one which will give sin, cos, tan, cube and factorial
else:
    len(numbers) == 2 # when input is 2 numbers
    print calculator.xy_function(numbers[0],numbers[1]) #run function two which gives add, subtract, multiply, divide and exponential (2 numbers)

