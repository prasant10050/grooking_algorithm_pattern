# Given a non-empty array containing unique integers and a target sum,
# you have to write a function that should return an array containing
# any two unique numbers from the input array; however,
# if there are no pair of numbers that sum up to the target sum,
# the function should return an empty array.
#
# Example:
#
# Array: [-2, 5, 6, 3, 4, 5, 9, 7]
#
# Target sum: 14
# 
# Output: [5, 9] # [9, 5] works as well, but you can’t add an integer to itself
# so [7, 7] does not worka

def pair_with_target_sum_by_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sums = nums[left] + nums[right]

        if sums == target:
            return [left, right]
        if target > sums:
            left += 1
        else:
            right -= 1
    return [-1, 1]


def pair_with_target_sum2_by_index(nums, target):
    mapping = {}

    for index, value in enumerate(nums):
        diff = target - value
        if diff in mapping:
            return [mapping[diff], index]
        else:
            mapping[value] = index


def pair_with_target_sum(nums, target):
    result = pair_with_target_sum_by_index(nums, target)
    if result[0] and result[1] == [-1, -1]:
        return
    return [nums[result[0]], nums[result[1]]]


def pair_with_target_sum2(nums, target):
    result = pair_with_target_sum2_by_index(nums, target)
    if result is None:
        return
    return [nums[result[0]], nums[result[1]]]


if __name__ == '__main__':
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum2([2, 5, 9, 11], 11))
