from itertools import permutations


def print_all_possible_concatenations_string(string_list):
    all_concatenations = []

    def recursive_concatenation(current, remaining):
        if not remaining:
            all_concatenations.append(current)
        else:
            for i in range(len(remaining)):
                recursive_concatenation(current + remaining[i],
                                        remaining[:i] + remaining[i + 1:])

    recursive_concatenation('', string_list)
    return all_concatenations


def find_all_concatenations(strings):
    all_concatenations = []

    def backtrack(current, remaining):
        if not remaining:
            all_concatenations.append(current)
        else:
            for i in range(len(remaining)):
                backtrack(current + remaining[i],
                          remaining[:i] + remaining[i + 1:])

    backtrack('', strings)
    return all_concatenations


def concat_list4(lst):
    def helper(lst, i, j):
        if i == len(lst):
            return [lst[j]]
        if j == len(lst):
            return helper(lst, i + 1, 0)
        if i != j:
            return [lst[i] + lst[j]] + helper(lst, i, j + 1)
        return helper(lst, i, j + 1)

    return helper(lst, 0, 0) + lst


# initializing list
test_list = ['hello', 'world', 'python']


def main():
    print("All possible concatenations in strings")
    print(print_all_possible_concatenations_string(test_list), end=" ")
    print("----------------------------------")
    print(find_all_concatenations(test_list), end=" ")
    print("----------------------------------")
    print(concat_list4(test_list), end=" ")


# printing original list
print("The original list : " + str(test_list))

# All possible concatenations in String List
# Using permutations() + loop
temp = []
for idx in range(1, len(test_list) + 1):
    temp.extend(list(permutations(test_list, idx)))
res = []
for ele in temp:
    res.append("".join(ele))

# printing result
print("All String combinations : " + str(res))
print("----------------------------------")
if __name__ == "__main__":
    main()
