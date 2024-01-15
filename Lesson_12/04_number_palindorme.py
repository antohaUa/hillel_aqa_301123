# Given an integer x, return true if x is a palindrome , and false otherwise.
# Input: x = 121
# Output: true
x = 13231  #


# true

# x = 1234  # -> false

def is_palindrome(num):
    return True if str(num) == str(num)[::-1] else False


print(is_palindrome(x))
