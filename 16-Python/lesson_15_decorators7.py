def hello():
    return "Hi JOSE!"

def other(func):
    print("Hello JOSE!")
    print(func())    #=> will function if it want to print

other(hello) #=> print hello funtion
#=> Hello JOSE!
#=> Hi JOSE!