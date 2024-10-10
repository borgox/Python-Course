# 1. Write a Python program that asks the user for two numbers 
# using the method input() (wich you can assign to a variable) and 
# prints their sum, difference, product, and quotient.


# Ask the user for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the numbers to float numbers
num1 = float(num1)
num2 = float(num2)

# Perform operations

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 # Remember not to divide by 0

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")


# 2. Program to evaluate the expression a + b * c and (a + b) * c 
# with given values:

# Variables
a = 4
b = 7
c = 2

# Evaluate the expressions
result1 = a + b * c
result2 = (a + b) * c

# Print the results
print(f"a + b * c = {result1}")
print(f"(a + b) * c = {result2}")

# 3. Program to check if a number is between 10 and 20 (inclusive) 
# using logical operators:

# Ask for a number
num = input("Enter a number: ")

# Convert the number to int
num = int(num)

# Check if the number is between 10 and 20
if 10 <= num <= 20:
    print(f"The number {num} is between 10 and 20.")
else:
    print(f"The number {num} is not between 10 and 20.")
    
    
# 4. Program to increase the value of a variable by 10
# and multiply it by 3 using assignment operators:

# Initialize variable
x = 5  # or any other value

# Perform operations using assignment operators
x += 10  # Increase x by 10
x *= 3   # Multiply x by 3

# Print the result
print(f"The new value of x is: {x}")


# 5. Program to perform a bitwise AND operation on two numbers 
# provided by the user:

# Ask the user for two numbers
num1 = input("Enter the first number (integer): ")
num2 = input("Enter the second number (integer): ")

# Convert numbers to int
num1 = int(num1)
num2 = int(num2)

# Perform bitwise AND operation
result = num1 & num2

# Print the result
print(f"The result of bitwise AND between {num1} and {num2} is: {result}")