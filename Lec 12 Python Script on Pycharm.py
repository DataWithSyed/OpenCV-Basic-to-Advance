x = "Hello World"
y = 'My Name is Taha'
z = 'Sohail\'s Sister' # if you use single quotes and apostrophe at a same time so the middle quote will be written with \ backslash
print(x)    print(y)    print(z)
name = "hello "
print(name.capitalize()) # Intellescence which is provided by Pycharm and it means when you write something pycharm will suggest you some supporting code
head = "    Class, 8, stand, up "
print(head.upper())
print(head.lower())
print(head[0]) # this is indexing calling 1st letter of a word by [0]
print(head[0:3])  # it will print fisrt three letter 0,1,2 and 4th (3) is not included
print(head.strip())  # strip means the spaces before and after a word will be removed
print(head.islower())  # islower is used to check whether the word is in lowercase
print(head.isupper())  # isupper is used to check whether the word is in uppercase
print(head.replace("C", "J"))  # replace is used to replace a specific alphabet from a Phrase or aw Word
print(head.split(','))  # used to split a word or to convert a Phrase into an array
print(len("hello"))  # if you have not assigned a variable then you can take directly string and change in it what you want
print(name * 100)