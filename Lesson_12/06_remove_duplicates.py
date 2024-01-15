# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums.
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# set
# len(list) - len(set)
l1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
unique_list = sorted(list(set(l1)))
print(unique_list)

# from itertools import zip_longest
# target_list = list(zip_longest(l1,unique_list, fillvalue='_'))
# print(target_list)


underscore_list = ['_'] * (len(l1) - len(unique_list))
print(underscore_list)
unique_list.extend(underscore_list)
print(unique_list)
