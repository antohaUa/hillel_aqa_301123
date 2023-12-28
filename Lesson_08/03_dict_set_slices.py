# flake8 inside Pycharm
# https://habr.com/ru/companies/dataart/articles/318776/

l1 = [1, 2, 3, 4]
print(l1[::-1])

# https://docs.python.org/3/library/itertools.html
# dict slices
d2 = {'1': 1, '2': 2, '3': 3, '4': 4}
from itertools import islice

print(dict(islice(d2.items(), 1, 3)))

# set slices
s1 = {1, 2, 3, 4, 5, 6, 7}
print(set(islice(s1, None, None, 2)))
