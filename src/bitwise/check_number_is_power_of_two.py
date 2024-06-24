# Write a program to check if a given number is a power of 2 or not.
def IsPowerOf2(n):
    return n != 0 and (n & (n - 1) == 0)


print(IsPowerOf2(6))
print(IsPowerOf2(8))
