print(1 >= 1) #=> True

print(1 <= 4) #=> True

print(1 == 1) #=> True

print(1 == '1') #=> False

print('hi' == 'bye') #=> False

print( 1 != 2) #=> True


#################### Logical Python ##################
print((1>2) and (2<3)) #=> False

if 1<2:
    print('yes!') #=> yes!

if 1<2:
    print('First Block')
    if 2<3:
        print("True!")
#=> First Block
#=> True!
        
if 1<2:
    print('First Block')
    if 20<3:
        print('Second Block')
#=> First Block
        
if 1 > 2 :
    print("Hello")
else :
    print("Last")
#=> Last
    
if 1 > 2:
    print("Hello")
elif 3 == 3:
    print("3 Equal 3")
else:
    print("Last")
#=>3 Equal 3
    
#################### For Loop ##################
seq = [1,2,3,4,5,6]

for item in seq:
    #Code here
    print('hello',item)
#=> hello 1
#=> hello 2
#=> hello 3
#=> hello 4
#=> hello 5
#=> hello 6
    
d = {"Sam":1, "Frank":2, "Dan":3}

for item in d:
    print(item)
#=>Sam
#=>Frank
#=>Dan
    
for item in d:
    print(item)
    print(d[item])
#=>Sam
#=>1
#=>Frank
#=>2
#=>Dan
#=>3
    
mypairs = [(1,2),(3,4),(5,6)]

for item in mypairs:
    print(item)
#=>(1, 2)
#=>(3, 4)
#=>(5, 6)
    
for (tup1,tup2) in mypairs:
    print(tup1)
    print(tup2)
#=>1
#=>2
#=>3
#=>4
#=>5
#=>6
    
for (tup1,tup2) in mypairs:
    print(tup2)
    print(tup1)
#=>2
#=>1
#=>4
#=>3
#=>6
#=>5
    
i = 1
while i < 5:
        print("i is: {}".format(i))
        i = i + 1
#=>i is: 1
#=>i is: 2
#=>i is: 3
#=>i is: 4

list1 = [1,2,3,4,5]
print(list1)
 #=>[1, 2, 3, 4, 5]
range1 = range(5)
print(range1)
#=>range(0,5)

print(list(range(0,5)))
#=>[0,1,2,3,4] index position

print(list(range(0,20,2)))
#=>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(list(range(0,21,2)))
#=>[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#List Comprehension
x = [1,2,3,4]

out = []
for num in x :
    out.append(num**2)# num **2 == 1^2, 2^2, 3^2, 4^2
print(out)
#=>[1, 4, 9, 16]

out = [num**2 for num in x]
print(out)
#=>[1, 4, 9, 16]

#################### Function ##################
def my_func(param1='default'):
    print("my first python function!")
my_func()
#=>my first python function!

def my_func(param1='default'):
    print("my first python function! {}".format(param1))
my_func()
#=>my first python function! default

#################### Comment in function ##################
def func():
    """
    THIS IS THE DOCSTRING
    fasdjfakdfjkal;dfs
    adfjaldjf;afja;ldf
    """
    print()

def hello():
    return "HELLO"
result = hello()
print(result)
#=> HELLO

def addNum(num1,num2):
    return num1+num2
result = addNum("2","3")
print(result)
#=>23

def addNum(num1,num2):
    return num1+num2
result = addNum("2","3")
print(type(result))
#=><class 'str'>

def addNum(num1,num2):
    return num1+num2
result = addNum(2,3)
print(type(result))
#=><class 'int'>

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"
    
result = addNum(2,3)
print(result)
#=>5

def addNum(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers!"
    
result = addNum("2",'3')
print(result)
#=>Sorry, I need integers!

#################### Lambda Expression ##################
# Filter
mylist = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0
evens = filter(even_bool,mylist)
print(list(evens))
#=>[2, 4, 6, 8]

print(evens)
#=><filter object at 0x100feef40>

#################### String ##################
str = "Hello"
print(str.lower()) #=> hello
print(str.upper()) #=> HELLO
print(str.split()) #=> ['Hello']

tweet = "Go Sports! #Sports"
result = tweet.split('#')
print(result)
#=>['Go Sports! ', 'Sports']

print('x' in [1,2,3,x])
#=> False

print('x' in [1,2,3,'x'])
#=> True