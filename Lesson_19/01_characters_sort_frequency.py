# Input:
# "tree"
#
# Output:
# "eert" "eetr"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

s1 = 'ttaaabbbbc'  # -> 'bbbbaaattc'

l1 = list(s1)
print(s1)

# in key functions we need create new list for key function
# to avoid existing list modification on the fly

l1.sort(key=lambda x: list(s1).count(x), reverse=True)
# l1.sort(key=list(s1).count, reverse=True)
print(''.join(l1))


# alternative solution
s2 = ''.join(sorted(s1, key=s1.count, reverse=True))
print(s2)

