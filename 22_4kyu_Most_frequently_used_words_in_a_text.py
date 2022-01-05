from numpy import copy


def sortByLength(inputStr):
    return len(inputStr)


def top_3_word(text):
    import re

    pattern = r"([a-zA-Z]+['-]?[a-zA-Z]+|[a-zA-Z])+"
    match = [x.lower() for x in re.findall(pattern, text)]
    directory = {}
    for i in match:
        if not i in directory:
            directory[i] = 1
        else:
            directory[i] += 1
    # print(directory)
    list_d = list(directory.items())
    list_d.sort(key=lambda i: i[1])
    if not directory:
        return []
    elif len(directory) == 1:
        return list(directory)
    elif len(directory) == 2:
        if len(list_d[-1][0]) > len(list_d[-2][0]) and list_d[-1][1] == list_d[-2][1]:
            return [list_d[-2][0], list_d[-1][0]]
        return [list_d[-1][0], list_d[-2][0]]

    list_d = list(directory.items())
    list_d.sort(key=lambda i: i[1])
    m = [list_d[-1]]
    for i in reversed(list_d):
        if i[1] == m[-1][1] or len(m) <= 3:
            m.append(i)
            continue
        if len(m) > 3:
            break
    m.pop(0)
    print("m", m)
    print(list_d)

    m = [list_d[-1][0], list_d[-2][0], list_d[-3][0]]
    m.sort(key=sortByLength)
    return m

    # return [list_d[-1][0], list_d[-2][0], list_d[-3][0]]


# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa


def top_3_words(text):
    import re

    # pattern = r"([a-zA-Z]+['-]{1}[a-zA-Z]+|['-]{1}[a-zA-Z]+['-]{1}|[']{1}[a-zA-Z]+|[a-zA-Z]+[']{1}|[a-zA-Z])+"
    # pattern = r"([a-zA-Z]*['-]?[a-zA-Z]+|[a-zA-Z]+['-]?[a-zA-Z]*|[']|[a-zA-Z])+"

    pattern = r"[']?[a-zA-Z]+['-]?[a-zA-Z]+[']?|[']?[a-zA-Z][']?"
    print(text)
    match = {}
    for i in re.findall(pattern, text.lower()):
        print(i, end="-")
        if i not in match:
            match[i] = 1
        else:
            match[i] += 1
    print("\n", match)
    print()
    list_d = list(match.items())
    # list_d.sort(key=lambda i: i[1])
    if len(list_d) == 2:
        return [list_d[-1][0], list_d[-2][0]]
    elif len(list_d) == 1:
        return [list_d[-1][0]]
    elif not list_d:
        return []
    # print(match[max(match.values())])
    l = []
    dictionary = match.copy()
    for i in range(3):
        for keys, values in dictionary.items():
            if values == max(match.values()):
                match.pop(keys)
                l.append([keys, values])
                break
        dictionary = match.copy()
    print(l)
    # return l
    # return [list_d[-1][0], list_d[-2][0], list_d[-3][0]]


print(top_3_words("In a village of La Mancha, the name of which I have no desire to call to\
mind, there lived not long since one of those gentlemen that keep a lance\
in the lance-rack, an old buckler, a lean hack, and a greyhound for\
coursing. An olla of rather more beef than mutton, a salad on most\
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra\
on Sundays, made away with three-quarters of his income."))
print(top_3_words("a a a a b b b b c c c e e e tt tt tt fas fas fas fads bdf"), ["a", "b", "c"])
print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("'f,   ,'ws ac' a' 'wrq q'q q'q dgs' dgs' ''hej 'gd''gd add’asd’aa’"))
