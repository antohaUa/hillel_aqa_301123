####################################################################################################################
# task 1
# how to check if string without spaces is palindrome 'Dogma I am God'
# (Reading left->right == right->left)
s1 = 'dogma i am god'
# s3 = ''.join(reversed(s1))
# print(s3)
# s1_r = s1.replace(' ', '')
# print(s1_r)
# # reverse string
# s2 = s1_r[::-1]
# print(s2)

assert s1.replace(' ', '') == s1.replace(' ', '')[::-1], 'Not a palindrome'


####################################################################################################################
# task 2
# count words in text and check if present words from banned lists.
# Replace banned words with '<censored>'

s2 = """
some small poem about old man and whale 
terrible story about fighting and surviving in weird and wild conditions  
"""
ban_list = ['terrible', 'weird', 'wild']

s2_split = s2.split()
print(s2_split)
print(len(s2_split))

find_index = s2_split.index(ban_list[0])
print(find_index)
assert find_index != -1, 'First ban word not found'
# print(s2_split[8])
s2_split[find_index] = '<censored>'
print(s2_split)
s_result = ' '.join(s2_split)
print(s_result)

####################################################################################################################
# task 3
# create dict with 0 values for each digit
# count digit appearance in given string and add this count values to created dict
s1 = '34234235245341231231231238900'
import string

digits = string.digits
print(digits)
d1 = dict.fromkeys(digits, 0)  # no keyword value=smth -> just default value after as keys object
print(d1)
d1['0'] = s1.count('0')
d1['1'] = s1.count('1')
d1['2'] = s1.count('2')
d1['3'] = s1.count('3')
d1['4'] = s1.count('4')
print(d1)


####################################################################################################################
# How to solve tasks . Recommendations:

#  - algorithm
#  - dir(<type>) dir(str) , dir(list) etc
#  - help(str.split)
####################################################################################################################



