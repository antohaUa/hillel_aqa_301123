def get_sum(lst):
    """Returns the sum of a list of integers"""
    total = 0
    for i in lst:
        breakpoint()
        # import pdb; pdb.set_trace() # python under 3.7
        # print(total)                # debbuger for beginners )
        total += i
    return total


numbers = [1, 2, 3, 4, 5]
result = get_sum(numbers)
print('The sum of', numbers, 'is', result)
a=5
b=6
print('End')
