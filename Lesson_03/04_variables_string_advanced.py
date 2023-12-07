# multiple variables in one line
x, y, z = 's1', 's2', 's3'

print(x, y, z)

a = 5
b = 10
a, b = b, a   # change variable values a=10, b=5
print(a, b)

# string - immutable type
var1 = 'Sample Text'
var1 = var1.lower()
print(type(var1))
print(var1)
print(id(var1))
var1 = 12
str2 = (f'{var1}-------------------------------------------------------------'
        f'------------{var1}adfdfsssssssssssssssssssssssssssssssssssssssssssf'
        'asdasdasdas555')
idx = str2.find('\n')
print(idx)
print(str2)

print('Can\'t')
print("Can't")
