def count_subarrays_with_sum_equals_k(nums,k):
    count =0
    current_sum=0
    prefix_sum={0:1}

    for num in nums:
        current_sum+=num
        count+=prefix_sum.get(current_sum-k,0)
        prefix_sum[current_sum]=prefix_sum.get(current_sum,0)+1
    return count

if __name__=="__main__":
    print(count_subarrays_with_sum_equals_k([1, 1, 1],2))