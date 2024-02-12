# write script that will read "input.txt" file and find there all characters from english alphabet
# collect these characters and their positions in file
# after info collected this info as text write to "output.txt" file in such format
# ####################
# <first found letter> -> pos1
# <next_letter> -> pos2
# <next_letter -> pos3
# etc
# #######################
import re

with open('input.txt', 'rt') as in_fh:
    content = in_fh.read()

letters_iterator = re.finditer(r'[a-zA-Z]', string=content, flags=re.MULTILINE)
output = []
for curr_match in letters_iterator:
    # print(curr_match)
    # #print(curr_match.string)
    # print(curr_match.start())
    # print(dir(curr_match))
    output.append(f'{curr_match.group(0)} -> {curr_match.start() + 1}')

with open('output.txt', 'wt') as out_fh:
    out_fh.write('\n'.join(output))
