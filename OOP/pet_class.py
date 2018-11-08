class Pets:
    dogs= []
    
    def __init__(self, dogs):
        self.dogs = dogs

class Dog:
    family = "mammals"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def hungry_dog(self):
        self.is_hungry = False

my_dogs = [
    Dog ("Tom", 6),
    Dog ("Fletcher", 7),
    Dog ("Larry",9)
]

my_pets = Pets(my_dogs)

print("I have {} dogs".format(len(my_dogs)))
for dog in my_pets.dogs:
    print ("{} is {}" .format(dog.name, dog.age))
print ("And they are all {}, ofcourse".format(dog.family))
 
for dog in my_pets.dogs:
    if dog.is_hungry:
        print("My dogs are not hungry")
    else:
        print("My dogs are hungry")
