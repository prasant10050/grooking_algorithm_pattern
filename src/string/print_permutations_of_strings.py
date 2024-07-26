from itertools import permutations


def generate_permutations(str):
    return [''.join(p) for p in permutations(str)]


def main():
    str = "abc"
    print("All permutations of the string")
    print(generate_permutations(str), end=" ")


if __name__ == "__main__":
    main()
