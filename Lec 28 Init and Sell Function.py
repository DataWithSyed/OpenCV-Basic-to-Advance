class Car:              #this will create a class
    def __init__(self, speed=200, color='black', transmission='manual'):         # __init__ behaves like self constructor and is initializer for the class
        print(speed)
        print(color)
        print(transmission)
        self.speed = speed      # assignment of attributes 
        self.color = color
        self.trasmission = transmission
        print("The __init__ is called")             # this print 3 times because we create 3 objects


print("*************Another Method Creating Instance of Class************")

# How to create an instance of a class

ford = Car(200, 'red', 'manual')            # this will create an object or instance of a class
honda = Car(400, 'blue', 'automatic')
audi = Car(350, 'black', 'automatic')

ford.speed = 200        # This will create attribute of object
honda.speed = 220
audi.speed = 250
ford.color = 'red'        # This will create attribute of object
honda.color = 'blue'
audi.color = 'black'

ford.transmission = 'manual'        # This will create attribute of object
honda.transmission = 'automatic'
audi.transmission = 'automatic'

ford.speed = 300                    # speed, color and transmission are data
ford.color = 'Blue'
print(ford.color,':' , ford.speed, ':' ,ford.transmission)

