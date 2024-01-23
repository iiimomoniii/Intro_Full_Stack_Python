mylist = [1,2,3]
mylist.append(4)
print(mylist) #=> [1, 2, 3, 4]

print(type(mylist)) #=> <class 'list'>
print(type(200)) #=> <class 'int'>
print(type(20.0)) #=> <class 'float'>

# ------------ Class ----------- #
class Sample ():
    pass

x = Sample()
print(type(x)) 
#=> <class '__main__.Sample'>

# ------------------------------ #
# Class
class Dog():

    def __init__(self,breed):
        self.breed = breed

mydog = Dog(breed = "Lab")
otherdog = Dog(breed = "Huskie")
print(type(mydog))
#=> <class '__main__.Dog'>
print(mydog.breed)
#=> Lab
print(otherdog.breed)
#=>Huskie

# ----------------------------- #
# Class
class Dog():

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab", name = "sammy")
otherdog = Dog(breed = "Huskie", name = "anny")
print(type(mydog))
#=> <class '__main__.Dog'>
print(mydog.breed)
#=> Lab
print(mydog.name)
#=> sammy
print(otherdog.breed)
#=> Huskie
print(otherdog.name)
#=> anny

# ----------------------------- #
# Class
class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

mydog = Dog(breed = "Lab", name = "sammy")
print(mydog.species)
