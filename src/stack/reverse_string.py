from stack import Stack


def reverse_string(stack, string):
    for i in range(len(string)):
        stack.push(string[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


stack = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(stack, input_str))
