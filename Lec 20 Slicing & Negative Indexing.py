# Slicing means to get any data from a specific list or set or matrix to make a new set of data

a = [0,1,2,3,4,5,6,7,8,9]
b = (0,1,2,3,4,5,6,7,8,9)
c = '0123456789'

# you can use slice function with list, tupples or strings or sets
# x = slice(start, end, step)
x = slice(0, 8, 2)
print(a[x])

# Short Notation or Another method of representing slice
print(a[0:9:2])

# it will print from 1st element to last element
print(a[0:])

# It will print all element
print(b[:])

# It will print from 1st element to the 2nd last element
print(c[:9])

# Negative indexing means calling elements from right not from left
print(a[-1:])
print(a[1::-1])
