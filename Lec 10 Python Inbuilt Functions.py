# Python InBuilt Functions and Modules

# Inbuild function: input, int, print, float, str, format, max, min
# for list of all inbuilt functions
print(dir(__builtins__))

# for power we have learned in previous lecture 2 ** 3 or 2 e 3 or 2 E 3
print(pow(2,3))

# for length of string and integers
print(len("Hello"))

# to find the info about the function written as argument of help
print(help(max))
print(max(7,8,2,6,3,14,5,2,5,55,5,5,8,9,4,2,6))

# Built-in Modules
# How to import a built-in module in python and use them

# for math module
import math
print(math.sqrt(81))
print(help(math.sqrt))

# If you want to look for all functions built inside math module
print(dir(math))
