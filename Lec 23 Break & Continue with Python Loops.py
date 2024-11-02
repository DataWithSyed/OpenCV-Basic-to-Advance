# BREAK & CONTINUE
# We use BREAK mostly in loops and is used to terminate loop at any instant condition
# For BREAK
a = [0,1,2,3,4,5,6]
for x in a:
    if x == 4:
        break
    print(x)
print('-------------------------------------------------')
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
print('-------------------------------------------------')
# For CONTINUE
a = [0,1,2,3,4,5,6]
for x in a:      # in for loop, if continue is used it will skip the condition like in this case is x==4
    if x == 4:
        continue
    print(x)
print('-------------------------------------------------')
i = 0
while i < 5:     # in while loop, if continue is used it will stop before the condition like in this case is i==3
    if i == 3:
        continue
    print(i)
    i += 1
