# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving
# the order of characters. No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"    e -> a  g->d
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true

# s = 'paper'
# t = 'title'
# s = "foo"
# t = "bar"

s = 'air'
t = 'AIR'


def check_isomorphic(s1, s2):
    if len(s1) == len(s2):
        table_translation = str.maketrans(s1, s2)
        result = s1.translate(table_translation)
        if result == s2:
            return True
    return False


res = check_isomorphic(s, t)
print(res)
