t1 = (3, 4, 5, 6)
print(t1[0:4])
print(t1[0:4:-1])  # () ??  -> # print(t1[0:4][::-1]) correct
print(t1[::-1])

"""
The slice of s from i to j with step k is defined as the sequence
 of items with index x = i + n*k such that 0 <= n < (j-i)/k.
 In other words, the indices are i, i+k, i+2*k, i+3*k and so on,
 stopping when j is reached (but never including j).
 When k is positive, i and j are reduced to len(s) if they are greater.
 When k is negative, i and j are reduced to len(s) - 1 if they are greater.
 If i or j are omitted or None, they become “end” values (which end depends on the sign of k).
 Note, k cannot be zero. If k is None, it is treated like 1.
"""
# https://docs.python.org/3/library/stdtypes.html#typesseq
