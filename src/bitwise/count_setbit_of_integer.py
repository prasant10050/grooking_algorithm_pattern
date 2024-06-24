# Write a program to count set bits of an integer.
#
# Input: 125
#
# Output: 6
# Explanation: Input has six 1’s or set-bits so the output will be 6.

# What are set-bits?
# 1 = set-bit
#
# 0 = unset-bit

def helper(n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
            ans += 1
        n //= 2
    return ans


def bitwiseHelper(n):
    count = 0
    while n > 0:
        if (n & 1) == 1:
            count += 1
        n >>= 1
    return count


def optimiseBitwiseHelper(n):
    count = 0
    while n > 0:
        count += (n & 1)
        n >>= 1
    return count


# Brian Kernighan’s algorithm#

def CountSetBits(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count


number = 125
print("SetBit count is: ", helper(number))
print("SetBit count is: ", bitwiseHelper(number))
print("SetBit count is: ", optimiseBitwiseHelper(number))
print('SetBit Count is: ', CountSetBits(number))


def counting_bits(n):
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = CountSetBits(i)
    return ans


n = 3
print(counting_bits(n))
# Write a program to return an array of number of 1’s in the
# binary representation of every number in the range [0, n].
