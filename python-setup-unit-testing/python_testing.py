# Write a simple Python script with at least two functions that perform different operations.

# function called subtract_numbers takes 2 parameters, 
# subtracts them and returns the result
def subtract_numbers(a,b):
    return a - b

# function called divide_numbers takes 2 parameters, 
# checks if the 2nd parameter is equal to zero (will result in ZeroDivisionError)
# if not, the parameters are divided against each other and returned
def divide_numbers(a,b):
  if b != 0:
    return a / b
  else:
    return 'cannot divide by zero'

# print('subtract_numbers(3,2) equals: ' + str(subtract_numbers(3,2))) # expected: 1
# print('subtract_numbers(10,-2) equals: ' + str(subtract_numbers(10,-2))) # expected: 12


# print('divide_numbers(20,2) equals: ' + str(divide_numbers(20,2))) # expected: 10
# print('divide_numbers(0,10) equals: ' + str(divide_numbers(0,10))) # expected: 0
# print('divide_numbers(10,0) equals: ' + str(divide_numbers(10,0))) # expected: 'cannot divide by 0' message