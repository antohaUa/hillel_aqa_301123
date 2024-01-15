# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# understand how many characters


# for
# startwith

l1 = ['flower', 'flow', 'flight' ]
# find shortest string
l2 = l1.copy()
l2.sort(key=lambda x: len(x))
print(l2)
shortest_el = l2[0]
print(shortest_el)

output = ''
for idx, _ in enumerate(shortest_el):
    target_prefix = shortest_el[:idx + 1]
    # print(target_prefix)
    if all([curr_el.startswith(target_prefix) for curr_el in l1]):
        # print(f'All elements started with {target_prefix}')
        output = target_prefix
    else:
        break

print(f'Output longest prefix = "{output}"')


# alternative solution #2
iter_obj = min(l1, key=lambda x: len(x))
prefix = ''
for i in range(len(iter_obj) + 1):
    if all([el.startswith(iter_obj[:i]) for el in l1]):
        prefix = iter_obj[:i]
print(f'{prefix=}')
