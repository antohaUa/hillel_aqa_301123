import string

s1 = '12312312grn'
s2 = s1.rstrip(string.ascii_letters)
i1 = int(s2)
print(i1)
