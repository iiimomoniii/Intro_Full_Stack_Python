import re

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Search fot pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'This is a string with numbers 1233221 and a symbol #hastag'

test_patterns = [r'\W+']

multi_re_find(test_patterns,test_phrase)

# test_patterns = [r'\d+']
# => 1233221

# test_patterns = [r'\D+']
# => ['This is a string with numbers ', ' and a symbol #hastag']

# test_patterns = [r'\S+']
# => ['This', 'is', 'a', 'string', 'with', 'numbers', '1233221', 'and', 'a', 'symbol', '#hastag']

# test_patterns = [r'\W+']
# => [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']