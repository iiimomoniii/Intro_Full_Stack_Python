# def new_decorator(func):
#     def wrap_func():
#         print("CODE HERE BEFORE EXECUTING FUNC") #fisrt 
#         func() #second follow func need to print in case func_needs_decorator 
#         print("FUNC() HAS BEEN CALLED") #last

#     return wrap_func

# def func_needs_decorator():
#     print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

#=> CODE HERE BEFORE EXECUTING FUNC
#=> THIS FUNCTION IS IN NEED OF A DECORATOR!
#=> FUNC() HAS BEEN CALLED


# use decorator

def new_decorator(func):
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC") #fisrt 
        func() #second follow func need to print in case func_needs_decorator 
        print("FUNC() HAS BEEN CALLED") #last

    return wrap_func

@new_decorator #=> use decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


func_needs_decorator()
#=> CODE HERE BEFORE EXECUTING FUNC
#=> THIS FUNCTION IS IN NEED OF A DECORATOR!
#=> FUNC() HAS BEEN CALLED