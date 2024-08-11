def remove_white_spaces(s):
    if s is None or s[0] == '\0':
        return

    # We will use read, write pointers here.
    # Write pointer will follow the read pointer
    # and only write characters read that are neither
    # a space (' ') nor a tab ('\t').
    read_ptr = 0
    write_ptr = 0

    while read_ptr < len(s) and s[read_ptr] != '\0':
        if s[read_ptr] != ' ' and s[read_ptr] != '\t':
            s[write_ptr] = s[read_ptr]
            write_ptr += 1
        read_ptr += 1
    return ''.join(s[:write_ptr])


def main():
    str_list = ["All greek to me.", "We love Python", "You are amazing"]
    for i in range(len(str_list)):
        print(str(i + 1) + ".     Actual string:                ", str_list[i])
        arr1 = list(str_list[i])
        print("       String without spaces or tabs:",
              remove_white_spaces(arr1))
        print("-" * 100)


if __name__ == '__main__':
    main()
