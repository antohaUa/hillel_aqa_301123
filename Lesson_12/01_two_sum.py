# https://leetcode.com/problems/
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
l1 = [2, 7, 11, 15]
target = 9

l2 = [3, 2, 4]
target2 = 6

l3 = [3, 3]
target3 = 6


def solution(target_list, target_sum):
    output = []
    for idx, el in enumerate(target_list):
        # print(el)
        expected_el = target_sum - el
        # print(f'Expected el = {expected_el}')
        # print(expected_el in target_list)
        if expected_el in target_list:
            idx2 = target_list.index(expected_el)
            if idx != idx2:
                output.append(idx)
                # print(f'{idx=}')
                # print(f'{idx2=}')
                output.append(idx2)
                break
    return output


# idx , el
# target _el = target_sum - el
# check if element in our list and idx != current index of iteration
# output -> idx, idx2


print(solution(l1, target))
print(solution(l2, target2))
print(solution(l3, target3))
print('=' * 50)


def alt_solution(target_list, target_sum):
    output = []
    for idx, el in enumerate(target_list):
        expected_el = target_sum - el
        found_idx2 = [idx2 for idx2, el in enumerate(target_list) if el == expected_el and idx != idx2]
        if found_idx2:
            output.append(idx)
            output.append(found_idx2[0])
            break
    return output


print(alt_solution(l1, target))
print(alt_solution(l2, target2))
print(alt_solution(l3, target3))
