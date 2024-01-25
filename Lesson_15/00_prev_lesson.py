# lambda a: a + 2
# [lambda a: a + 2, 9, 3, 1, 0]

def lambda1(a):
    return a + 2

# lmbd1 = lambda a: a + 2

num = 9
l1 = [lambda1, num, 3, 1, 0]
int_and_float = [el for el in l1 if type(el) in (int, float)]
print(int_and_float)

print(lambda1(int_and_float[0]))

# ###################################

t1 = (3, 4, 5, 6)
print(t1[0:4])
# print(t1[0:4:1])
# print(t1[0:4:2])
print(t1[0:4:-1])  # ??
print(t1[::-1])



# ###################################
fh = open('some.txt', 'w+')
fh.write('Smth\n')
fh.write('SmthOther\n')
fh.seek(0)
data = fh.read()
print(data)
fh.close()
