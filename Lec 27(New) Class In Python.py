class Rectangle:
    pass

rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 20
rect2.height = 30

rect1.width = 40
rect2.width = 10

print(rect1.height * rect1.width, 'sq.meters')
print(rect2.width * rect2.height, 'sq.meters')

