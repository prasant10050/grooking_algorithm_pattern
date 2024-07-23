def find_repeated_sequences(s, k):
    n = len(s)
    if n < k:
        return set()

    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    a = 4
    numbers = []
    for i in range(n):
        numbers.append(mapping.get(s[i]))

    hash_value = 0
    hash_set = set()
    output = set()

    for i in range(n - k + 1):
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (a ** (k - j - 1))
        else:
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (
                        a ** (k - 1))) * a) + numbers[i + k - 1]

        if hash_value in hash_set:
            output.add(s[i: i + k])

        hash_set.add(hash_value)

    return output


def main():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC",
                     "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()
