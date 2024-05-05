from stack import Stack


def is_match(char1, char2):
    if char1 == "(" and char2 == ")":
        return True
    elif char1 == "{" and char2 != "}":
        return True
    elif char1 == "[" and char2 == "]":
        return True
    else:
        return False


def is_parentheses_balanced(string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(string) and is_balanced:
        paren = string[index]
        if paren in '([{':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
            index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
