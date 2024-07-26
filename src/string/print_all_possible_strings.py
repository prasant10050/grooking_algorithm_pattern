from itertools import permutations


def print_all_possible_string(str):
    n = len(str)
    combos = (1 << n)

    # Generate all possible combinations
    for i in range(1, combos):
        current_combination = ""
        for j in range(n):
            if i & (1 << j):
                current_combination += str[j]
        current_combination = sorted(current_combination)
        for perm in permutations(current_combination):
            print("".join(perm), end=" ")


def main():
    str = "abc"
    print("All permutations of the string")
    print(print_all_possible_string(str), end=" ")


if __name__ == "__main__":
    main()
