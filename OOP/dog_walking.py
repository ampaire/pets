class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


class Dog:

    family = 'mammals'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
         return ("{} is walking!".format(self.name))

my_dogs = [
    Dog ("Tom", 6), 
    Dog ("Fletcher", 7), 
    Dog ("Larry", 9)
]
my_pets = Pets(my_dogs)
my_pets.walk()