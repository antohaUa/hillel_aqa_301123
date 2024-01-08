# https://docs.python.org/3/reference/compound_stmts.html#for

from collections.abc import Iterable

print(isinstance(1231, Iterable))  # check if integer iterable
print(isinstance('1231', Iterable))  # check if string iterable

# -------------------------
for character in 'Hello world!':
    print(character, end='  ')
print(f'\n"{character}"')

# underscore "_" we use if variable value not used inside cycle
for _ in 'Hello':
    print('1', end='  ')
print('\n')

for idx, _ in enumerate('Hello'):
    print(idx, end='  ')
print('\n')

# enumerate
print()
print(tuple(enumerate((1, 3, 5, 7), start=0)))
#                     0  1  2  3
for itm in enumerate((1, 3, 5, 7), start=100):
    print(itm, end='  ')
print()
for num in range(11):
    print(num)

# dictionaries
print()
d1 = {'a': 1, 'b': 2, 'c': 3}
# 1 keys
for itm in d1:
    print(itm) if itm != 'a' else print(itm * 2)
# 2 keys
for itm in d1.keys():
    print(itm) if itm != 'a' else print(itm * 2)
# 3 values
for itm in d1.values():
    print(itm) if itm != 2 else print(itm * 2)
# 4 tuple = ( key, value)
for itm in d1.items():
    print(itm)

# Christmas tree
for i in range(1, 10):
    print(f'{" * " * i:^40}')

# some example
s1 = "Amazing string with positive mood"
for ch in s1.lower():
    if 'a' <= ch <= 't':
        print(ch, end='')

# break
for idx, val in enumerate(range(0, 11)):
    print(val)
    if idx == 5:
        print('Middle')
        break

# continue
print('=' * 30)
for idx, val in enumerate(range(0, 11)):
    print('Begin of iteration')
    if idx == 5:
        print('Middle')
        print('Iteration interruption')
        continue  # break fro current iteration
    print(idx)
    print('End of iteration')
    print('*' * 40)

# else
print('=' * 30)
l1 = []
for el in l1:
    print(el)
    if el == 1:
        break
else:
    print('No elements')
