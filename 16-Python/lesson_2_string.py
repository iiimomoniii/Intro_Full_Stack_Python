# String
myString = 'abcdefghijklmnopqrstuvwxyz'
myString1 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
print(myString) #=> abcdefg
#Indexing
print(myString[2]) #=> c
#Slicing
print(myString[3:]) #=> defghijklmnopqrstuvwxyz
print(myString[:4]) #=> abcd
print(myString[2:5]) #=> cde
print(myString[::2]) #=> a,(b),c,(d),e,(f),g  acegikmoqsuwy
print(myString[::3]) #=> a,(b),(c),d,(e),(f),g  adgjmpsvy


print(myString.upper()) #=> ABCDEFGHIJKLMNOPQRSTUVWXYZ


print(myString.capitalize()) #=> Abcdefghijklmnopqrstuvwxyz


print(myString1.split()) #=> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Basix Methods
x = "Item One : {x}, Item Two: {x}".format(x="dog",y="cat")
print(x)

