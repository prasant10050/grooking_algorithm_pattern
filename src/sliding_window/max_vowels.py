def max_vowels(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # initialise our state variables
    vmax = -1     # maximum number of vowels seen in a subatring
    smax = ''     # the substring in which we found the maximum
    # iterate over all the possible substrings, which start from positions 0 to len(s)-k
    for i in range(len(s)-k+1):
        # extract the substring
        substr = s[i:i+k]
        # count the number of vowels
        num_vowels = sum(1 if c in vowels else 0 for c in substr)
        # is it a new maximum count? if so, update our state
        if (num_vowels > vmax):
            vmax = num_vowels
            smax = substr
    # all substrings visited, return the one with the most vowels
    return smax

print(max_vowels('sfjfio', 3))
print(max_vowels('ioosdfghjkaeibnffbjfbnfoii', 4))
