# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# merge
# sort
l1 = [1, 2, 4]
l2 = [1, 3, 4]

l3 = l1.copy()
l3.extend(l2)
l3.sort()
# l3.sort(key=lambda x: x, reverse=False)
print(l3)

l4 = sorted(l1 + l2)
print(l4)
