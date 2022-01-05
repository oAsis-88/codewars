def valid_parentheses(string):
    string = "".join([x for x in string if x == '(' or x == ')'])
    while '()' in string:
        string = string.replace('()', '')
    return string == ''


print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
