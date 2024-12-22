# Problem:
# Given an array of positive integers and a target sum, find the minimal length
#
# Example:
# Input: target=7, nums=[2, 3, 1, 2, 4, 3]
# Output: 2 (Subarray: [4, 3])
#

def min_subarray_len(target,nums):
    left=0
    current_sum=0
    min_length=float('inf')

    for right in range(len(nums)):
        current_sum+=nums[right]
        while current_sum>=target:
            min_length=min(min_length,right-left+1)
            current_sum-=nums[left]
            left+=1

    return min_length if min_length!=float('inf') else 0

if __name__=="__main__":
    print(min_subarray_len(7,[2, 3, 1, 2, 4, 3]))