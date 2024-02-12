# #############################################################################
# write generator function that has as input some range value and chunk_size
# produces output as lists with len == chunk size
# Example:
# Call:  chunk_generator(range(11), chunk_size=3) ->
# Output:  [0, 1, 2]
#          [3, 4, 5]
#          [6, 7, 8]
#          [9, 10]
# #############################################################################

def chunk_generator(target_range, chunk_size=3):
    l1 = list(target_range)
    l1_len = len(l1)
    int_num = l1_len // chunk_size
    rest = l1_len % chunk_size
    int_num = int_num + 1 if rest else int_num
    # print(f'{int_num=}')
    for i in range(1, int_num + 1):
        #  0       1       2      3
        #  1       2       3      4
        # 1 2 3  4 5 6   7 8 9  10 11
        # 0 1 2  3 4 5   6 7 8  9 10
        # 0
        # Output:  [0, 1, 2]
        #          [3, 4, 5]
        #          [6, 7, 8]
        #          [9, 10]
        #
        yield l1[(i - 1) * chunk_size:chunk_size * i]

    # for el in target_range:
    #     yield el


g1 = chunk_generator(range(11), chunk_size=3)
for i in g1:
    print(i)
