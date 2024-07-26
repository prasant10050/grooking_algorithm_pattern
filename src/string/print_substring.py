def print_substring(str):
    n = len(str)

    for i in range(n):
        for j in range(i, n):
            sub_string = str[i:j + 1]
            print(sub_string)

def print_substring_by_length(str,k):
    n = len(str)

    for i in range(n-k+1):
        for j in range(i, i+k):
            sub_string = str[i:j+1]
        print(sub_string)

print_substring("abcd")

print("------------------")

print_substring_by_length("abcd",3)
