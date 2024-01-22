myList = [1,2,3,4,5,6,7,8,9,0]
print(myList) #=> [1,2,3,4,5,6,7,8,9,0]
print(len(myList)) #=> 10
# -------------------------- #

myList2 = ['a','b','c']
print(myList2[2]) #=> c
myList2[0] = 'New Item'
print(myList2) #=> ['New Item', 'b', 'c']
myList2.append('Append Item')
print(myList2) #=> ['New Item', 'b', 'c', 'Append Item']
myList2.append(['Append List','x', 'y', 'z'])
print(myList2) #=> ['New Item', 'b', 'c', 'Append Item', ['Append List', 'x', 'y', 'z']]
print(myList.pop(0)) #=> 0
# -------------------------- #

myList1 = ['a','b','c','d','e','f','g']
print(list(reversed(myList1))) #=>['g', 'f', 'e', 'd', 'c', 'b', 'a']
# -------------------------- #

myList3 = [1,5,2,1,5,73,45,7,4,79,45,2]
print(list(sorted(myList3))) #=>[1, 1, 2, 2, 4, 5, 5, 7, 45, 45, 73, 79]
# -------------------------- #

myList4 = [1,2,['x','y','z']]
print(myList4[2][1]) #=> y

myList5 = [[1,2,3],[4,5,6],[7,8,9]]
# LIST COMPREHENSION
first_col = [row[0] for row in myList5]
print(first_col) #=> [1, 4, 7]