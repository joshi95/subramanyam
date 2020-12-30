def is_bal(str):
    stack = list()

    for c in str:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    return False

if __name__ == '__main__':
    str = "(((()()(())"
    print(is_bal(str))

