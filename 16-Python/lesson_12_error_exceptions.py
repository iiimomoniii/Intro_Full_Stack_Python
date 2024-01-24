try:
    f = open('/16-Python/errors_exceptions/simple.txt','r')
    f.write("Test write to simple text!")
except IOError:             #=> exception
    print("ERROR : COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()
print("hello world!")