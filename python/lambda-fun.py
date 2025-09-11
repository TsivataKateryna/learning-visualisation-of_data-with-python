import math as mt

'learning lambda-function'

square = lambda x: x**2
print(square(5)) 

add = lambda a, b: a + b
print(add(3, 7))






numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
