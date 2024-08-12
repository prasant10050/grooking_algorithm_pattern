#  977. Squares of a Sorted Array (Easy)
#
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
def sortedSquares(nums):
    smallerValueIdx = 0
    largerValueIdx = len(nums) - 1
    sortedsquares = [0 for _ in nums]

    for idx in reversed(range(len(nums))):
        smallerValue = nums[smallerValueIdx]
        largerValue = nums[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedsquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedsquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedsquares


if __name__ == '__main__':
    print(sortedSquares([-4, -1, 0, 3, 10]))
    print(sortedSquares([-7, -3, 2, 3, 11]))
