P = {0: 1, 1: 1}


def partitions(n):
    if n in P:
        return P[n]
    num = 0

    for k in range(1, n):
        k1 = int(n - (3 * k ** 2 - k) / 2)
        if k1 >= 0:
            if k1 not in P:
                P[k1] = partitions(k1)
            num += (-1) ** (k - 1) * P[k1]
        else:
            return num

        k2 = int(n - (3 * k ** 2 + k) / 2)
        if k2 >= 0:
            if k2 not in P:
                P[k2] = partitions(k2)
            num += (-1) ** (k - 1) * P[k2]
        else:
            return num

    return num


for i in range(0, 26):
    a = partitions(i)
    print(i, " - ", a)
