import re

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Search fot pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string! But is has punctuation. How can we remove it?'

test_patterns = ['[A-Z]+']

multi_re_find(test_patterns,test_phrase)

# test_patterns = ['[^!.?]+']
#=> ['This is a string', ' But is has punctuation', ' How can we remove it']

# test_patterns = ['[a-z]+']
#=> ['his', 'is', 'a', 'string', 'ut', 'is', 'has', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']

# test_patterns = ['[A-Z]+']
#=> ['T', 'B', 'H']
