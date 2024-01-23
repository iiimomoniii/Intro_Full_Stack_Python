x = 25

def my_func():
    x = 50
    return x

print(x)
#=> 25
print(my_func())
#=> 50
my_func()
print(x)
#=> 25

############## Variable Scope ###############
#Local
lambda x: x**2

#Enclosing function locals
name = 'This is a global name!'

def greet():
    name = "sammy"

    def hello():            # hello() is not function inside greet()
        print("hello "+name)

greet()
#=>

# ------------------------------- #
name2 = 'This is a global name2!'

def greet2():
    name2 = "sammy2"

    def hello2():            
        print("hello "+name2)

    hello2() #hello2() is function inside greet()

greet2() 
#=>hello sammy2

# ------------------------------- #
name3 = 'This is a global name3!' # <= 

def greet3():
    name3 = "sammy3" 

    def hello3():            
        print("hello "+name3) # if print inside function that will call name3 == sammy3 before name3 = 'This is a global name3!'

    hello3()

greet3() 
#=>hello sammy3

# ------------------------------- #
name4 = 'This is a global name4!' # <= 

def greet4():
    #name4 = "sammy4" <= comment

    def hello4():            
        print("hello "+name4) 

    hello4()

greet4() 
print(name4) # if print outside function that will call name4 = 'This is a global name4!' before name4 == sammy4  
#=>hello This is a global name4!

# ------------------------------- #
x = 99

def func(x):
    print('x is:',x)
    x = 1000
    print('local x changed to:',x)

func(x)
print(x) #<= print global because find global name is x before x inside function 
#=> x is: 99
#=> local x changed to: 1000
#=> 99

# ------------------------------- #
x = 99

def func():
    global x 
    x = 1000

print("before function call, x is: ",x) 
func()
print(x)
#=> before function call, x is:  99 # <= discover x = 99 before x = 1000
#=> 1000 # <= when call function that find from inside to outside then discover x = 1000 before x = 99