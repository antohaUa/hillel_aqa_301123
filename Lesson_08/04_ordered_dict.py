# https://docs.python.org/3/library/collections.html#collections.OrderedDict
from collections import OrderedDict

od1 = OrderedDict({'1': 1, '2': 2, '3': 3, '4': 4})
print(od1)
od1.move_to_end('1', last=True)
print(od1)
od1.move_to_end('3', last=False)
print(od1)
print(od1['3'])

# where could be used ?
# https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
# Web page parsing for example if we shold understand what data was last inserted

