#GLOBAL VARIABLE
s = 'GLOBAL VARIABLE!'
def func(s):
    print(s)

func(s)
#=> GLOBAL VARIABLE!

s = 'GLOBAL VARIABLE!'
def func(s):
    s=50 #=> reset global variable and assign new value
    print(s) 

func(s)
#=>  50

s = 'GLOBAL VARIABLE!'
def func():
    global s #=> call global without send parameter to function
    s=50 #=> reset global variable and assign new value
    print(s) 

func() #=> not send variable to function
#=>  50