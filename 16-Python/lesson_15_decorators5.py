def hello(name="Jose"):
    return "hello "+name

print(hello())
# => hello Jose

def hi(name="Jone"):
    return "hi "+name
newFunc = hi #=> automatic change variable to function

print(newFunc()) #=> newFunc is new function
#=> hi Jone

def outside():
    print("HELLO outside")

    def inside(): #=> not call inside
        return "THIS STRING IN inside"
    
outside()
#=> HELLO outside 

def outside():
    print("HELLO outside")

    def inside():
        return "THIS STRING IN inside"
    print(inside()) #=> print function inside
    
outside()
#=> HELLO outside
#=> THIS STRING IN inside
