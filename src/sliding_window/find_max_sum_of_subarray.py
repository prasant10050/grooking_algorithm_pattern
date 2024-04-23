def find_average_of_subarray(k, arr):
    print("init find_average_of_subarray")
    windowSum, windowStart = 0.0, 0
    maxSum = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def find_average_of_subarray_method2(k, arr):
    windowSum = sum(arr[:k])
    maxSum = windowSum

    for i in range(k, len(arr)):
        windowSum = windowSum - arr[i - k] + arr[i]
        maxSum = max(windowSum, maxSum)
    return maxSum


if __name__ == "__main__":
    print(find_average_of_subarray(3, [2, 1, 5, 1, 3, 2]))
    print(find_average_of_subarray_method2(3, [2, 1, 5, 1, 3, 2]))
