# Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element is distinct.
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
#
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
###############################

# get all duplicates

# set

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
set1 = set(nums)
result = len(nums) == len(set1)
print(result)

unique_duplicates = []
for el in set1:
    # print(el)
    count = nums.count(el)
    if count > 1:
        unique_duplicates.append(el)

unique_duplicates2 = [el for el in set(nums) if nums.count(el) > 1]
print(unique_duplicates)
print(unique_duplicates2)
