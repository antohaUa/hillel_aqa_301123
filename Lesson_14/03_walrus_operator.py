# :=
text = 'Some string to split'

print(text.split())
print(''.join(text.split()))
print(len(''.join(text.split())) / len(text.split()))

operations = {
    'words': text.split(),
    'letters_count': len(''.join(text.split())),
    'avg_letters_per_word': len(''.join(text.split())) / len(text.split())
}

operations2 = {
    'words': (words := text.split()),
    'letters_count': (l_count := len(''.join(words))),
    'avg_letters_per_word': l_count / len(words)
}
#
print(operations)
print(operations2)


def func(x):
    return x ** 2


lc = [func(itm) for itm in range(11) if func(itm) < 100]
lc2 = [res for itm in range(10) if (res := func(itm)) < 100]
# print(res)
print(lc)
print(lc2)

# regexp
import re

s1 = 'Hello World'
if result := re.match(r'^[hH]ello [wW]orld', s1):
    print(bool(result))


# 1922 -> 1+9+2+2 -> 14 -> 1+4 => 5
def magic_digit2(number):
    curr_num = number
    # current_len = len(str(curr_num))
    while current_len := len(str(curr_num)) > 1:
        curr_num = sum([int(ch) for ch in str(curr_num)])
        # current_len = len(str(curr_num))
        print(curr_num)
        print(current_len)
    return curr_num


print(magic_digit2(1922))
