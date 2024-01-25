def outside(name = "jose"):
    def hello():
        return "THIS IS STRING FROM hello()"
    def hi():
        return "THIS IS STRING FROM hi()"
    if name == "jose":
        return hello #=> return value in function hello
    else :
        return hi
    
x = outside()
print (x())
#=> THIS IS STRING FROM hello()