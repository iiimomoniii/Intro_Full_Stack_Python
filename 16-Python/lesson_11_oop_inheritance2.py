class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return "hello"

b = Book("Python","jose", 200)
print(b)
#=> hello

mylist = [1,2,3]
print(mylist)
#=> [1, 2, 3]

# ------------------------------------- #
class Book2():
    def __init__(self,title2,author2,pages2):
        self.title2 = title2
        self.author2 = author2
        self.pages2 = pages2
    
    def __str2__(self):
        return "Title2: {}, Auther2: {},Pages2: {}".format(self.title2,self.auther2,self.pages2)

c = Book2("Python2","jose2", 2002)
print(c)
#=> hello