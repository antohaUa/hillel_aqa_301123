# https://docs.python.org/3/reference/compound_stmts.html#if
if True:
    print('Yes')

x1 = -100
if x1 < 0:
    x1 = -x1
    if x1 == 100:
        print('Bingo!')
print(x1)

# double comparison
x2 = 7
if 10 > x2 > 2:  # x2<10 and x2>2
    print(f'{x2} between 2 and 10')

# and
# 1  0  -> 0
# 0  1  -> 0
# 1  1  -> 1


# and or not
x3 = 12
if x3 % 3 == 0 and x3 % 4 == 0 and 60 // x3 == 5:
    print('All fine')
#
if (x3 % 3 == 1) or ((x3 % 4 == 0) and (60 // x3 == 5)):
    print('All fine, but...')

# if (x3 % 3 == 1):
#     if (x3 % 4 == 0):
#         ...

#
# in operator  ( related to iterators)
if ('a' in 'Map'):
    print('a found')
# if 5 in 4435345345:
#     print('5 found')     # error 'int' is not iterable

# boolean types
empty_tuple = tuple()
print(type(empty_tuple))
empty_dict = {}
print(type(empty_dict))
print(f'Empty tuple = {bool(())}')
print(f'Empty string = {bool("")}')
print(f'Empty list = {bool([])}')
print(f'Empty set = {bool(set())}')
print(f'Empty dict = {bool({})}')
#
d1 = {'a': 1}
print(bool(d1))
if d1:
    print('Not empty')

s1 = ''
if not s1:
    print('String has empty value')

l1 = [100, 200]
l1.pop()
l1.pop()
if l1:
    print('Not empty')
#
# wrong
val1 = None  # is None
print(None == False)
print(bool(None) == False)
print(bool(val1))

# best practices
print(val1 is None)
if not val1:  # not False == True
    print('We should do smth with this')

condition1 = -5 > 0
condition2 = -10 > 1
condition3 = -11 > 1

if condition1:
    print(1)
elif condition2:
    print(2)
elif condition3:
    print(3)
else:
    print(4)

# max for three numbers
x, y, z = 300, 100, 50
if x > y:
    if x > z:
        print('X')
    else:
        print('Z')
else:
    if y > z:
        print('Y')
    else:
        print('Z')

# ternar if
a = 5
b = 10
# block         condition                 else else block
print('Yes') if (a < b) and (b % 10 == 0) else print('No')

# the same
# if (a < b) and (b % 10 == 0):
#     print('Yes')
# else:
#     print('No')

print(f'b is {("round" if (b % 10 == 0) else "not round")} number')
#
# ternar max from three numbers but not the best practice
x, y, z = 370, 200, 350
max_num = (x if x > z else z) if x > y else (y if y > z else z)
print(max_num)
