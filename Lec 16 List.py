# list is a kind of collection which allows us to put many values in a single variable
# Members inside a a lists are called Elements

x = [3,4,2,8,2,7,5]
print(x)

print(x[1])

y = [8,7,2,6,9,2,6]
print(y)

print(x[5] + y[0])

z = ['Taha', 4, 5.3, [8, 5]]
print(z)

print(len(x))

# want to insert new element into pre-defined list
x.insert(2, 'Sohail')
print(x)

# want to remove an element
z.remove('Taha')
print(z)

# if you have duplicates in your list then element is removed from left
y.insert(1, 8)
print(y)

y.remove(8)
print(y)

# if you want to remove an element from the last then
x.pop()
print(x)

# if you want to delete a whole list
del z
#print(z)

# want to remove all the elements from a list
y.clear()
print(y)

# to sort all these integers inside a list in a Ascending Order
x1 = [8,2,4,5,2,5,24,6]
x1.sort()
print(x1)

# sorting integers inside a list in a Descending Order
x1.reverse()
print(x1)

# if you want to add an element in the last
x1.append(88)
print(x1)

# want to make duplicate of a list
s = x1.copy()
print(s)

# want to count number of elements in a list
print(x1.count(87))
