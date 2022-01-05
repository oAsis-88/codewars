def validBraces(string):
    stack = []
    for i in string:
        stack.append(i)
        if len(stack) > 1:
            if (stack[-2] == '{' and stack[-1] == "}") \
                    or (stack[-2] == '(' and stack[-1] == ")") \
                    or (stack[-2] == '[' and stack[-1] == "]"):
                stack.pop()
                stack.pop()
    if len(stack) == 0:
        return True
    return False


print(validBraces("()"))
print(validBraces("[(])"))
