def remove_duplicates_sorted_array(arr):
    next_non_duplicate = 1
    i = 1
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate


def remove_duplicates_unsorted_array(arr, target_key):
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != target_key:
            arr[next_element] = arr[i]
            next_element += 1
    return next_element


if __name__ == '__main__':
    print(remove_duplicates_sorted_array([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates_sorted_array([2, 2, 2, 11]))

    print(remove_duplicates_unsorted_array([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_duplicates_unsorted_array([2, 11, 2, 2, 1], 2))
