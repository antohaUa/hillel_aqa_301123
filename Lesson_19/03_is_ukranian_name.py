# filter from list names that have only ukranian characters
ukrainian_letters = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'"
ukr_letters_set = set(ukrainian_letters)

names = ['Bob', 'Петро', 'Соломія', 'Эдуард']
# iterate over names
# name1 = 'Петро'
# set1 = set(name1)
# set3 = set1 - set2
lc1 = [el for el in names if not (set(el) - ukr_letters_set)]
print(lc1)

name1 = 'ПетроZ'
lc2 = [letter for letter in name1 if letter not in ukrainian_letters]
print(lc2)




