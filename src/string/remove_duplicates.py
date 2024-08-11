def remove_duplicates(_str):
    hashset = set()

    writeIndex = 0
    readIndex = 0

    # Iterates loop till end of strinng
    while readIndex < len(_str):
        if _str[readIndex] not in hashset:
            hashset.add(_str[readIndex])
            # calls helper function to iterate remaining string
            _str[writeIndex] = _str[readIndex]
            writeIndex += 1
        readIndex += 1

    result = _str[:writeIndex]
    return result


def main():
    str_list = ["dabbac", "aabbbccdddeee", "abcdef"]
    for i in range(len(str_list)):
        print(str(i + 1) + ".     Before: ", str_list[i])
        str_list[i] = list(str_list[i])
        result = remove_duplicates(str_list[i])
        print("       After:  ", ''.join(result))
        print("-" * 100)


if __name__ == '__main__':
    main()
