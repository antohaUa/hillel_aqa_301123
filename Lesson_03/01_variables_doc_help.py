magic_num = 11321  # use readable variables names

# remember that some names are reserved by python
# get list of available built-in functions
# -----------------------------------------
import builtins

print(*dir(builtins), sep='\n')
# -----------------------------------------
# list keywords
# -----------------------------------------
from keyword import kwlist

print('\n'.join(kwlist))
# -----------------------------------------
# [DOC & help]
# https://docs.python.org/3/library/string.html

v1 = object
print(help(dir))
print(*dir(v1), sep='\n')
print(repr(v1))

# get list of available modules
# -----------------------------------------
help('modules')
