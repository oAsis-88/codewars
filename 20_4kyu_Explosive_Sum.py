def exp_sum(n, directory):
    if n in directory:
        return directory[n]
    else:
        result = 0
        num = 0
        for i in range(0, n):
            if i in directory:
                result += (-1) ** (i // 2) * directory[i]  # exp_sum(i, directory)
            else:
                exp_sum(n - i - 1, directory)
        directory[n] = result
    return


directory = {0: 1, 1: 1}

n = 5
exp_sum(n, directory)


def func(n, directory):
    if n in directory:
        return directory[n]
    count = 1
    result = 0
    for i in range(0, n):
        print((-1) ** (i // 2))
        directory[i] = func(i)
        count += 2
    return directory[n]
