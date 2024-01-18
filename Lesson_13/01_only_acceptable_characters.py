# Given string  of characters
# Check that all characters are from ascii table
# starting from space character(32) and finishing ~ character(126)
# return true or false
s1 = '🦊 sdf45435324 🦆'  # -> False
s2 = 'Super String~'  # -> true

# 'a' < 'b' < 't'
# get bool value for each character
result = all([' ' <= el <= '~' for el in s2])
print(result)
