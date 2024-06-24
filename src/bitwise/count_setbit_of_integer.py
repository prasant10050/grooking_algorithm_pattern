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


number = 125
print("SetBit count is: ", helper(number))
print("SetBit count is: ", bitwiseHelper(number))
print("SetBit count is: ", optimiseBitwiseHelper(number))
