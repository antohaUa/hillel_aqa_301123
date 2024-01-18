# Given an integer num, repeatedly add all its digits until
# the result has only one digit, and return it.
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

num = 1922  # -> 1922 ->  14 - > 5


# while  n_lenght > 1
# make string
def magic_digit(number):
    curr_num = number
    current_len = len(str(curr_num))
    while current_len > 1:
        str_num = str(curr_num)
        list_num = [int(ch) for ch in str_num]
        curr_num = sum(list_num)
        current_len = len(str(curr_num))
    return curr_num


def magic_digit2(number):
    curr_num = number
    current_len = len(str(curr_num))
    while current_len > 1:
        curr_num = sum([int(ch) for ch in str(curr_num)])
        current_len = len(str(curr_num))
    return curr_num


# alternative solution
def magic_digit3(number):
    result = number
    while result > 9:
        result = sum([int(el) for el in str(result)])
    return result


print(magic_digit(num))
print(magic_digit2(num))
print(magic_digit3(num))
