# Cередній показник по групі - 68%
# На цей показник впливає виконання ДЗ групою.
# Виконання ДЗ вище 90% - відмінно, виконання ДЗ 80-90% - добре, нижче 80% - погано.
# Середній показник по групах цього курсу — 71.


# marks 0-100
# <50  - not working code at
# [80-90] code has algorithm issues
# [90-99] linter/ optimization error, incorrect used structures
# 100 - all great!


# string copy
s1 = '1234'
s2 = s1  # immutable type

# list copy
l1 = [1, 2, 3, 4]
l2 = l1.copy()
l3 = l1[:]
l4 = [el for el in l1]

# dict copy
d1 = {'1': 1, '2': 2, '3': 3}
d2 = d1.copy()
d3 = dict(d1)
d4 = {**d1}
d5 = {k: v for k, v in d1.items()}

from copy import copy

l5 = copy(l1)

l1 = [1]
i1 = iter(l1)
# print(len(i1))
l1.append(2)
l1.append(3)
print(f'Calculated iterator length={i1.__length_hint__()}')
l1.append(4)
print(f'Calculated iterator length={i1.__length_hint__()}')
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))

# zip
ll1 = ['Bob', 'Alice', 111]
ll2 = [2, 22, 222, 555, 888]
ll3 = [0, 1, 2, 4]

ll4 = list(zip(ll1, ll2, ll3))
print(ll4)

# Practice Task
# 1-30 list comprehension get all number except numbers that have digit 3 inside
lc1 = [el for el in range(1, 31) if not '3' in str(el)]
print(lc1)
