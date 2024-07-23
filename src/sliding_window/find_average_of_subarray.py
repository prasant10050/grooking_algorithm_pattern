def find_average_of_subarray(k, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k - 1:
            result.append(windowSum / k)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result


def find_sum_of_array_upto_k(k, arr):
    windowSum = sum(arr[:k])
    return windowSum


if __name__ == "__main__":
    print(find_average_of_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
    print(find_sum_of_array_upto_k(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
