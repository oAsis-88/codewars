def decompose(n):
    for i in range(n):
        if n ** 2 - i * (i + 1) * (2 * i + 1) / 6 == 0:
            return [x for x in range(1, i+1)]
        elif n ** 2 - i * (i + 1) * (2 * i + 1) / 6 < 0:
            return i

    return n ** 2


for i in range(100):
    print(i, "-", decompose(i))
