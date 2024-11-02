# If duplicate elements are not present
A = {1, 2, 5, 87, 3, 26, 6}
print(A)

# If duplicate elements are present
b = {1, 2, 3, 5, 1, 2, 8, 6, 4, 7, 89, 25, 5, 8, 5, 5, 7}
print(b)

# to find the length or number of elements in a set
print(len(b))

# To insert/add an element in a set
b.add(10)
print(b)

# Want to add multiple elements in a set
A.update([15, 18, 17, 11])
print(A)

# if you want to remove an element
b.remove(89)
print(b)

# Similar to remove (if an element is not present in a set, then it will not give me an error)
A.discard(17)
print(A)

# If you want to remove any random element from a set mostly from the
# left
A.pop()
print(A)

# Method of Writing a Set
name = {'taha', 'sohail', 'omer', 'ezaan'}
print(name)
# another method to represent a set called Set Constructor
name1 = set(('taha', 'sohail', 'omer', 'ibrahim'))
print(name1)

# Conversion of set to list
z = set([1,2,3,4,5,6,7,8,9])
print(z)

# Mathematical Set operations like union, intersetion, difference
x = {8,4,0,2,3,1,5,6,7,9,8,3,0,1,4,2,5,8,6}
y = {11,12,13,15,14,18,19,16,17,20}
print(x)
print(y)

# for union of two sets
print(x | y)
print(x.union(y))

# for intersection of sets
print(x & y)
print(x.intersection(y))

# Difference between two sets
print( x - y )          # another method is  print(a.difference(b))
print(y - x)

# symmetric difference between two sets
print(x ^ y)
print(x.symmetric_difference(y))

# set are not indexed or in ordered
#print(x[2])

# for all function with sets
print(dir(x))
