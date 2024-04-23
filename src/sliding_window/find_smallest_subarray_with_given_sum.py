import math


def smallest_subarray_with_given_sum(s, arr):
    windowStart = 0
    min_length = math.inf
    windowSum = 0.0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        while windowSum >= s:
            min_length = min(min_length, windowEnd - windowStart + 1)
            windowSum -= arr[windowStart]
            windowStart += 1
    if min_length == math.inf:
        return 0
    return min_length


if __name__ == "__main__":
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
