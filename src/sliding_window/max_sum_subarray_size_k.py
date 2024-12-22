def max_sum_subarray_size_k(nums, k):
    max_sum=current_sum=sum(nums[:k])
    for i in range(k,len(nums)):
        current_sum+=nums[i]-nums[i-k]
        max_sum=max(max_sum,current_sum)
    return max_sum

if __name__ == "__main__":
    print(max_sum_subarray_size_k([2, 1, 5, 1, 3, 2], 3))

# Find the maximum sum of any subarray of size k.