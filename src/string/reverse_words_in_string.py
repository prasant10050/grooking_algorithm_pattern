def str_rev(_str, start, end):
    if _str is None or len(_str) < 2:
        return
    while start < end:
        _str[start], _str[end] = _str[end], _str[start]
        start += 1
        end -= 1


def reverse_words(sentence):
    if sentence is None:
        return "String is either null or empty"

    #  To reverse all words in the string, we will first reverse
    #  the string. Now all the words are in the desired location, but
    #  in reverse order: "Hello World" -> "dlroW olleH".
    str_len = len(sentence)
    str_rev(sentence, 0, str_len - 1)

    start = 0
    end = 0

    while True:

        # find the  start index of a word while skipping spaces.
        while start < len(sentence) and sentence[start] == ' ':
            start += 1

        if start == str_len:
            break

        # find the end index of the word.
        end = start + 1
        while end < str_len and sentence[end] != ' ':
            end += 1

        # let's reverse the word in-place.
        str_rev(sentence, start, end - 1)
        start = end


def main():
    string_to_reverse1 = list("Hello World!")
    print("1.    Actual string:   " + "".join(string_to_reverse1))
    reverse_words(string_to_reverse1)
    print("      Reversed string: " + "".join(string_to_reverse1))
    print(
        "-----------------------------------------------------------------------------------------------------")
    string_to_reverse2 = list("The quick brown fox jumped over the lazy dog.")
    print("2.    Actual string:   " + "".join(string_to_reverse2))
    reverse_words(string_to_reverse2)
    print("      Reversed string: " + ("".join(string_to_reverse2)))
    print(
        "-----------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
