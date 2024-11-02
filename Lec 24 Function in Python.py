# Function is a group of statements within a program that performs a specific task
# Functions are of two types which are
# 1. In-built functions like print, input, float, int, min, max
# 2. User Defined functions

def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give me the args of same type")
        return
    return(arg1 + arg2)             # print(arg1 + arg2) then no printing of the given values
a = sum(4,89)
print(a)
print(sum('Hello ', 'Taha'))       # This will concatenate because of + sign
print(sum(5.3, 9.8))
print(sum("Heloo", 55))

# Function makes your code simpler
# It makes your code usable multiple times
# You can test or debugg your code in a better way
