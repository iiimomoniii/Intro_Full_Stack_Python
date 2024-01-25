s = 'GLOBAL VARIABLE!'

def func():
    local = 10
    print(locals())
    print(globals())

func()
# => locals() = local dictionary
# => {'local': 10}

# => globals() = global dictionary
# => {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1031f4ca0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/natdanai/Documents/Projects/Udemy/Intro/16-Python/lesson_15_decorators3.py', '__cached__': None, 's': 'GLOBAL VARIABLE!', 'func': <function func at 0x1032f0430>}
