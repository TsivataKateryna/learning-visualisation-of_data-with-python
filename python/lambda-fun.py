
'''
A file for studying lambda functions in Python.

Contains:
- simple lambda functions
'''

from functools import reduce
import math as mt

square = lambda x: x**2
# print(square(5)) 

add = lambda a, b: a + b
# print(add(3, 7))

'Calculating the factorial of a number (using recursion and the ternary operator).'
# factorial = lambda a: 

''' 
Determining whether a number is even or odd.
'''
isEven = lambda a: True if a % 2 == 0 else False 
# print(isEven(1)) # false
# print(isEven(2)) # true
# print(isEven(0)) # true
# print(isEven(-3)) # false
# print(isEven(1000000000)) # true
# print(isEven(100000000000000001)) # false

'Random Functions'
function_1 = lambda x: (x-3)**2
function_2 = lambda x, y: (x-3)**2 - mt.sqrt(y)
# function_3 = 

'Calculating the sum of the squares of the elements in a list.'
list_numbers = [1, 2, 3, 4]
sum_squares = sum(map(lambda x: x**2, list_numbers))


'Calculating the arithmetic mean of a list of numbers.'


# numbers = [1, 2, 3, 4]
# squared_numbers = list(map(lambda x: x**2, numbers))
# print(squared_numbers)
