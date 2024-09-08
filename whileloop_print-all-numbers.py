# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

# Solution:

# Initialize the variable
number = 1

# Use a while loop to go through the range 1 to 1000
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1