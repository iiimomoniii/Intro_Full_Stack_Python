import re

def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("Search fot pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd..dsds..dssssss..sdddddd'

test_patterns = ['s[sd]+']

multi_re_find(test_patterns,test_phrase)


# test_patterns = ['sd*'] = find s follow d or more and keep 
# => ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sdddddd']

# test_patterns = ['sd+'] = find sd focus on s
# => ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sdddddd']

# test_patterns = ['sd?'] = find sd focus on s and sd
# => ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']

# test_patterns = ['sd{3}'] = find sd focus on s and only 3 ddd
# => ['sddd', 'sddd', 'sddd', 'sddd']

# test_patterns = ['sd{1,3}']
# => ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']

# test_patterns = ['s[sd]+']
# => ['sdsd', 'sssddd', 'sdddsddd', 'sds', 'ssssss', 'sdddddd']