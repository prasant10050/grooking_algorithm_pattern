# Write a program to check even or odd numbers.
#
# Let’s consider an array of integers here and check each of them using the AND operator.
#
# Input = {1, 2, 3, 4, 5, 6, 7, 8, 9}
#
# Output: { "Odd" , "Even" , "Odd" , "Even" , "Odd" , "Even" , "Odd" , "Even" , "Odd" }

def isEven(n):
    return "Even" if (n & 1) == 0 else "Odd"


def checkEvenOdd(array):
    result = []
    for n in array:
        result.append(isEven(n))
    return result


firstNumber = 125
secondNumber = 8
print("Number ", firstNumber, " is : ", isEven(firstNumber))
print("Number ", secondNumber, " is : ", isEven(secondNumber))

print(checkEvenOdd([1, 2, 3, 4, 5, 6, 7, 8, 9]))
