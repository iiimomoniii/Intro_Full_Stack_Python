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

