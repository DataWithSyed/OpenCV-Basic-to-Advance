# What is a variable? Answer: It is the storage location associated with symbolic name which may contains known or unknown info.
# Programmer choose the name of the variable
# Programmer can change the name of the variable in a later statement

myinfo = input("Give me a number: ")
print(myinfo.__len__())
print(type(myinfo))

# Rules of assigning variables :
# 1. Variable can't be a number or integer or string or float
# 2. Variables are case sensitive like when you are calling an assigned variable
# 3. Varibales are alphabets and may contain numbers or underscore
# 4. Variables cannot start with a number like 32Myinfo
# 5. Variables can start with underscore like _hero
# 6. Variables cannot start with intermediate special characters like alpha.22, alpha$32
# 7. You can't use reserved variables like def, if, else, elif, except, while, import, pass, is

# Exponent Function can be written as
exponent = 8e2
print(exponent)

exponent1 = 2E8
print(exponent1)

# for string assignment
myString = "Hey Gorgeous"
print(myString)

# Conversion of float to integer number
myInt = int(exponent)
print(myInt)

# Conversion Of Integer to Float number
myFloat = float(myInt)
print(myFloat)

# How to show the multiplication of two numbers and its result
print("8 * 9 = ", 8*9)

# Concatenation of more than one variables
print("Hello", " ", "World")

# New Method to show the multiplication of two variables
x = 50
y = 40
print("{0} * {1} = {2}".format(x, y, x * y))

# Printing any statement with separator
print("Hello", "World", sep="-----------")

# Using name of with greetings with modulo
name = input("Enter Your Name: ")
print("Good Day to %s" % name) # %s is used to print strings

age = int(input("Enter your age: ")) # Now we want to print name as well as age
print("Hello %s ! are you %d years old" % (name, age))  # %d is used to print integers and %f is used to print float point integers

# we want to print marks
marks = 922.6
print("Your marks are %f" % marks)

# if you want to limit decimal places
marks = 922.6
print("Your marks are %.2f" % marks) # if %f.2 then the result will be like 922.600000.2

# print("Heloo" + {name} + "nice to meet you")
