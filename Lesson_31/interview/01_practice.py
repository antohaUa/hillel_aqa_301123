# Input: i1 = 1631567
# Out:  {1: 'one', '2':"six"..., '7': 'seven'}

i1 = 45321
# Algorithm
numbers = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}
# int -> str
# enumerate


# raw code
s1 = str(i1)
result = {}
for idx, digit in enumerate(s1, start=1):
    result[idx] = numbers.get(digit)

print(result)

# optimized
result2 = {idx: numbers.get(digit) for idx, digit in enumerate(str(i1), start=1)}
print(result2)
