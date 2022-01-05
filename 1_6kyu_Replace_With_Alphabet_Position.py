def alphabet_position(text):
    array_text = list(text)
    result = ""
    for i in array_text:
        if (ord(i) < 65) or (ord(i) > 122) or (90 < ord(i) < 97):
            continue
        if ord(i) < 91:
            result += str(ord(i) - 64) + " "
        else:
            result += str(ord(i) - 96) + " "
    return result.strip()


print(alphabet_position("The sunset sets at twelve o' clock."))
