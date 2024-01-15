# we have two lists with equal or different size
# ex. l1=[1,3,5,7]  l2=[1,4,5]
# task:
# create list that will store such values list_target = [(1,1), (3,4), (5,5), (7,0)]
# zero (0) is our default value that we set if no such element by index was found in certain list.
# code should work and vise versa
# ex. l1=[1,4,5] l2=[1,3,5,7] input data should produce list_target = [(1,1), (4,3), (5,5), (0,7)]

# l1 = [1, 4, 5]
# l2 = [1, 3, 5, 7]
l2 = [1, 4, 5]
l1 = [1, 3, 5, 7, 9, 10]
default = 0

# [(1,1), (3,4), (5,5), (7,0)]

# len1 > len2
# then add zeros to l2
len1 = len(l1)
len2 = len(l2)
small_list = l1.copy() if len(l1) <= len(l2) else l2.copy()
big_list = l1.copy() if len(l1) >= len(l2) else l2.copy()
print(small_list)
print(big_list)
for i in range(0, len(big_list) - len(small_list)):
    small_list.append(default)
print(small_list)
target_list = list(zip(big_list, small_list))
print(target_list)

# alternative solution
from itertools import zip_longest

l3 = list(zip_longest(l1, l2, fillvalue=0))
print(l3)
