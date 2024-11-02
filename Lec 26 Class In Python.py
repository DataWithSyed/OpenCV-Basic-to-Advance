class Car:              #this will create a class
    pass

# How to create an instance of a class

ford = Car()            # this will create an object or instance of a class
honda = Car()
audi = Car()

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

print(honda.color, ':', honda.speed, ':', honda.transmission)
print(audi.color, ':', audi.speed, ':', audi.transmission)