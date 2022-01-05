def fib(n):
    print(n)
    arr = [0, 1]
    for i in range(1, n + 1):
        arr[0], arr[1] = arr[1], arr[0] + arr[1]
    return arr[1]


# Единичная матрица
def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


# Возведение матрицы в квадрат
def squaring_matrix(matrix_):
    return [[matrix_[j][0] * matrix_[0][i] + matrix_[j][1] * matrix_[1][i] for i in range(2)] for j in range(2)]


# Увеличение на 1 степень
def matrix(matrix_, end_matrix_, n):
    rank = 2
    n -= 1
    while n > 1:
        if rank >= n:
            n -= rank / 2
            rank = 2
            end_matrix_ = multiplication_matrix(end_matrix_, matrix_)
            matrix_ = [[1, 1], [1, 0]]
            continue
        matrix_ = squaring_matrix(matrix_)
        rank *= 2
        pass
    return end_matrix_[0][0]


def multiplication_matrix(mat1, mat2):
    return [[mat1[j][0] * mat2[0][i] + mat1[j][1] * mat2[1][i] for i in range(2)] for j in range(2)]
    pass


def fib_(n):
    print("n:", n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    matrix_ = [[1, 1], [1, 0]]
    end_matrix_ = [[1, 0], [0, 1]]
    rank = 2
    znak = 1
    if n < 0:
        if abs(n) % 2 == 0:
            znak = -1
        n = abs(n)
    while n > 1:
        if rank >= n:
            n -= rank / 2
            rank = 2
            end_matrix_ = multiplication_matrix(end_matrix_, matrix_)
            matrix_ = [[1, 1], [1, 0]]
            continue
        matrix_ = squaring_matrix(matrix_)
        rank *= 2
    return znak * end_matrix_[0][0]
    '''
    if n % 2 == 0:
        return matrix(matrix_, end_matrix_, n)
        pass
        # (b^(n/2))^2
    else:
        return matrix(matrix_, end_matrix_, n)
        pass
        # b * b^(n-1)
    '''


print(fib_(10000000))
print()

print(fib_(-4))
print()

'''
start = time.time()
print(fib(8192))
print("time 1:", time.time() - start)
start = time.time()
print(fib_(8192))
print("time 2:", time.time() - start)

print()
start = time.time()
print(fib(20000))
print("time 1:", time.time() - start)
start = time.time()
print(fib_(20000))
print("time 2:", time.time() - start)

print()
start = time.time()
print(fib(200000))
print("time 1:", time.time() - start)
start = time.time()
print(fib_(200000))
print("time 2:", time.time() - start)

print()
start = time.time()
print(fib_(2000000))
print("time 2:", time.time() - start)
'''
'''
print()
start = time.time()
print(fib(400000))
print("time 1:", time.time() - start)
start = time.time()
print(fib_(400000))
print("time 2:", time.time() - start)
'''
