import re

patterns = ['term1','term2']

text = ' This is a string with term1, not not the other! '

for pattern in patterns: # => Loop
    print(" I'm searching for : "+pattern)

    if re.search(pattern,text): # => Search (map text and pattern)
        print(" MATCH! ")
    else:
        print(" NO MATCH! ")

#=>  I'm searching for : term1
#=> MATCH!
#=> I'm searching for : term2
#=> NO MATCH!