#Inheritance
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) #<= inheritance Animal()
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

# mya = Animal()
# mya.whoAmI()
# mya.eat()
#=> ANIMAL CREATED     
#=> ANIMAL   
#=> EATING

myDog = Dog()
#=> ANIMAL CREATED
#=> DOG CREATED

myDog.bark()
#=> WOOF

myDog.whoAmI()
#=> ANIMAL #=> inside Animal()