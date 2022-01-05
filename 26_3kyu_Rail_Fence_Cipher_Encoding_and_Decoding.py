def encode_rail_fence_cipher(string, n):
    list_string = list(string)
    array = []
    steps = 2 * (n - 2) + 2
    for i in range(0, len(list_string), steps):
        array.append(list_string[i])
    for i in range(1, n - 1):
        for j in range(i, len(list_string), steps):
            array.append(list_string[j])
            array.append(list_string[j + steps - i * 2])
    for i in range(n - 1, len(list_string), steps):
        array.append(list_string[i])

    return "".join(array)


def decode_rail_fence_cipher(string, n):
    list_string = list(string)
    len_string = len(list_string)
    array = [""] * len_string

    steps = 2 * (n - 2) + 2
    lvl = 0
    tab = 0
    for i, el in enumerate(list_string):

        if steps * tab < len_string:
            array[lvl + steps * tab] = el
            tab += 1
        else:
            tab = 0
            lvl += 1

def test():
    print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3) == "WECRLTEERDSOEEFEAOCAIVDEN")
    print(encode_rail_fence_cipher("Hello, World!", 3) == "Hoo!el,Wrdl l")
    print(encode_rail_fence_cipher("", 3) == "")

    print(decode_rail_fence_cipher("H !e,Wdloollr", 4) == "Hello, World!")
    print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3) == "WEAREDISCOVEREDFLEEATONCE")
    print(decode_rail_fence_cipher("", 3) == "")


test()
