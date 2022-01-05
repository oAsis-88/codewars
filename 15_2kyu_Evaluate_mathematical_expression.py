def operand(n1, ch, n2):
    if ch == '+':
        return n1 + n2
    elif ch == '-':
        return n1 - n2
    elif ch == '*':
        return n1 * n2
    elif ch == '/':
        return n1 / n2


def calc(expression):
    print(expression)
    list_experession = list(expression)
    print(list_experession)
    for i in range(len(list_experession) - 2):
        if list_experession[i] == '-':
            j = i + 1
            if list_experession[j] == ' ':
                while list_experession[j] == ' ':
                    j += 1
            if list_experession[j] != '(' or (not list_experession[j].isdigit()):
                return "Invalid"
    stack = []
    list_experession = [x for x in list_experession if x != ' ']
    count = 0
    print(list_experession)
    if '(' in list_experession:
        for i in range(len(list_experession)):
            if list_experession[i] == '(':
                count = i
            if list_experession[i] != '(':
                continue
            else:
                if list_experession[i] != ')':
                    stack.append(list_experession[i])
                else:
                    stack.append(list_experession[i])
                    for j in range(len(stack)):
                        pass
                    break

    return expression


tests = [
    ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14],
    ["1 - - 1", "Invalid"],
    ["1- - 1", "Invalid"],
    ["6 + - (4)", "Invalid"],
    ["6 + -(- 4)", "Invalid"],
]

for test in tests:
    print(calc(test[0]) == test[1])
    print()
    print()

'''
print(expression)
    list_experession = list(expression)
    print(list_experession)
    for i in range(len(list_experession) - 1):
        if list_experession[i] == '-' and list_experession[i - 1] == ' ':
            j = i + 1
            if list_experession[j] == '(' or list_experession[j].isdigit():
                continue
            while list_experession[j] == ' ':
                j += 1
            if list_experession[j] == '(' or list_experession[j].isdigit():
                return "Invalid"
    stack = []
    list_experession = [x for x in list_experession if x != ' ']
    print(list_experession)
    for i in range(len(list_experession)):
        if list_experession[i].isdigit():
            num = list_experession[i]
            j = i + 1
            while list_experession[j].isdigit():
                num += list_experession[j]
                j += 1
            stack.append(num)
        if list_experession[i] == '+' or list_experession[i] == '-' or list_experession[i] == '*' or list_experession[i] == '/':
            j = i + 1
            if list_experession[j].isdigit():
                num = ""
                while list_experession[j].isdigit():
                    num += list_experession[j]
                    j += 1
                stack.append(operand(stack.pop(), list_experession[i], num))
'''
