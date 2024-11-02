#What are for loops? A for loop used to iterate over a sequence and that sequence can be a tuple,
#list or dictionary or a set or a string

a = [0,1,2,3,4,5,6]         # A list
b= (0,1,2,3,4,5,6)          # A tupple
c = (0,1,2,3,4,5,6)         # A set
d = '0123456'               # A string
e = {                       # A dictionary
    "first-name" : "Taha",
    "age" : 20,
    "last-name" : "Nasir",
    "college": "NED Univeristy of Engineering & Technology"
}
#How to use IN Operator? First it is used in for loops and can be
#used with tuple, list, dictionaries, sets or strings
#IN Operator is used to check whether the
#word after in operator is present in list or tuple or dictionary or set or strings

print(0 in a)
for x in a:
    print(x)

# Use for loop with dictionary: that means different for Dictionaries
for x in e.items():
    print(x)

# for printing a dictionary with coln and " "
for key, value in e.items():
    print(key, ' ', value)

# for printing any value with Range Function
for x in range(2, 25, 3):
    print(x)
else:
    print("Finished! ")
    
