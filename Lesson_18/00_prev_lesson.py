# iterators
# 0-5
# i1 = iter(range(6))
# next(i1)
for el in range(6):
    print(el)


# generators
# 0-5
def gen():
    for el in range(6):
        yield el
        print('Hello')


# i1 = iter(gen())
# next(i1)
for val in gen():
    print(val)
