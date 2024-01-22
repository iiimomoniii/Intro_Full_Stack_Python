x = set()
x.add(1)
x.add(2)
x.add(0.99)
print(x) #=> {0.99, 1, 2}

y = set()
y.add(2)
y.add(2)
y.add(2)
y.add(2)
y.add(3)
print(y) #=> {2, 3}

z = set([1,1,1,1,1,1,1,2,2,2,2,4,4,4,4,4,])
print(z) #=> {1, 2, 4}