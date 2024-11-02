# What is a loop?  A loop allow us to repeat some block of code again and again untill and unless some condition is met
# WHILE LOOP

# 1st Example
i = 0
while i < 5.6:
    print("The value of x is : ", i)
    i += 1
print("Finish")

#2nd Example
num = 1
sum = 0
print("Enter a Number. Please Enter zero(0) to exit")
while num != 0: # or can be written as True for infinetly
    num = float(input("Enter any number: "))
    sum = sum + num
    print(sum)

else:
    print("Finished Sum")