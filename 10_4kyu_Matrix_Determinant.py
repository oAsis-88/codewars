def det(minor):
    if len(minor) == 2:
        return minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
    array = [x for x in minor[0]]
    result = 0
    for i in range(len(array)):
        additional_minor = []
        for j in range(1, len(minor)):
            arr = []
            for k in range(len(minor)):
                if i != k:
                    arr.append(minor[j][k])
            additional_minor.append(arr)
        result += (-1) ** i * array[i] * det(additional_minor)
    return result


def determinant(matrix):
    if len(matrix[0]) == 0:
        return 0
    if len(matrix) == 1:
        return matrix[0][0]
    return det(matrix)


m1 = [[1, 3], [2, 5]]
m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]

print(determinant([[1]]))
print(determinant(m1))
print(determinant(m2) == -20)
print(determinant([[]]))

'''
test.assert_equals(determinant([[1]]), 1, "Determinant of a 1 x 1 matrix yields the value of the one element")
test.assert_equals(determinant(m1), -1, "Should return 1 * 5 - 3 * 2, i.e., -1 ")
test.expect(determinant(m2) == -20)
'''
