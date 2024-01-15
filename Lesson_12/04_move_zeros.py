# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
l1 = [0, 1, 0, 3, 12]

# get all that not zero
lc1 = [el for el in l1 if el != 0]
print(lc1)
zero_list = [0] * (len(l1) - len(lc1))
lc1.extend(zero_list)
print(lc1)

# alternative solution
l2 = [itm for itm in l1 if itm != 0]
num_zeros = l1.count(0)
# print(num_zeros)
l2.extend([0]*num_zeros)
print(l2)
