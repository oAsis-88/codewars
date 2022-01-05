def valid_solution(board):
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if board[i][j] == 0 or board[k][j] == 0 or board[i][k] == 0:
                    return False
                # print(i, j, "and", k, j)
                if k != i and board[i][j] == board[k][j]:
                    print("первый:", i, j, board[i][j], " ", k, j, board[k][j])
                    return False
                # print(i, j, "-and-", i, k)
                if k != j and board[i][j] == board[i][k]:
                    print("второй:", i, j, board[i][j], " ", i, k, board[i][k])
                    return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            array = []
            for k in range(3):
                for l in range(3):
                    array.append(board[k + i][l + j])
            if len(set(array)) != 9:
                return False
    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
