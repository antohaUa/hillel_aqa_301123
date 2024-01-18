#      0       1       2         3       4
l1 = ["az", "toto", "picaro", "zone", "kiwi"]

# [("az", "toto picaro zone kiwi"), ("az toto", "picaro zone kiwi"), ("az toto picaro", "zone kiwi")...

# ["az", "toto"]
# idx = 1
lslice = l1[:2]
print(lslice)

# ["picaro", "zone", "kiwi"]
# idx = 1
lslice2 = l1[2:]
print(lslice2)

#  slices [start:stop:step]
result = []
for idx, el in enumerate(l1):
    # idx = 0 -> 1 -> 2
    our_tuple = (' '.join(l1[:idx + 1]), ' '.join(l1[idx + 1:]))
    result.append(our_tuple)
result.pop()
print(result)

# alternative solution
lc = [(' '.join(l1[:i + 1]), ' '.join(l1[i + 1:])) for i in range(len(l1) - 1)]
print(lc)
