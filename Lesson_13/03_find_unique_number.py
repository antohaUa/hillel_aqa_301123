# Given an integer array nums, return true if present integer that has no second duplicate

# Example 1:
# Input: nums = [1,2,2,1,3]
# Output: true

# Example 2:
# Input: nums = [1,2,3,1,2,3]
# Output: false

# iter el and do count  == 1
nums = [1, 2, 2, 1, 3]
# nums = [1,2,3,1,2,3]
UNIQUE_COUNT = 1
unique_numbers = [el for el in nums if nums.count(el) == UNIQUE_COUNT]
print(True if unique_numbers else False)

# alternative solution
# | A | B | XOR Output |
# |---|---|------------|
# | 0 | 0 |     0      |
# | 0 | 1 |     1      |
# | 1 | 0 |     1      |
# | 1 | 1 |     0      |

#  (1^ 2^ 3) ^ (2 ^3 ^1) -> 0
a = 17
b = 17
print(a ^ b)  # 0

l2 = [1, 2, 2, 1]
result2 = 0
for el in l2:
    result2 ^= el
print(bool(result2))
