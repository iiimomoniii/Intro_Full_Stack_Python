s = 'GLOBAL VARIABLE!'

def func():
    local = 10
    print(locals())
    print(globals()['s']) #=> identify key from global variable

func()
# => locals() = local dictionary
# => {'local': 10}

# => globals() = global dictionary
# => GLOBAL VARIABLE! 