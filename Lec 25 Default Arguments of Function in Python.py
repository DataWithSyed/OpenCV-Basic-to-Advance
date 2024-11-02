# DEFAULT ARGUMENTS  **args  &  ***kwargs  IN PYTHON
# DEFAULT ARGUMENTS
def student(name='Unknown Name', age=0):
    print('name : ', name)
    print("age : ", age )
student('Taha', 20)
print('--------------------------------------------')
# If you call an empty function, then it will print default values which you assigned in the first step of def student
student()
print('--------------------------------------------')
student('Sohail')
print('--------------------------------------------')

# VARIABLE LENGTH ARGUMENTS
# single asteras * means you will use multiple arguments when you use this notation (it will give you tupple)
def student(name, age, **marks):
    # If you use double asteras ** then it will give dictionary
    print('Name : ', name)
    print('Age : ', age)
    print('Marks : ', marks)
    for key, value in marks.items():
        print(key, ' : ', value)
# if you use this notation, then always put thisat the end of your arguments

student('Taha', 20, English = 95, Maths = 80, Science = 50, Sociology = 64)