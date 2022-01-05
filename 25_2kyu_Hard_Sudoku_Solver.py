def create_squares_dict(squares):
    squares_dict = [{} for _ in range(9)]
    for element in range(9):
        for el in squares[element]:
            if type(el) == list:
                for e in el:
                    # print(squares_dict[element], e)
                    if squares_dict[element].__contains__(e):
                        squares_dict[element][e] += 1
                    else:
                        squares_dict[element][e] = 1
    return squares_dict


def create_row_dict(platform):
    row_dict = [{} for _ in range(9)]
    for element in range(9):
        for el in platform[element]:
            if type(el) == list:
                for e in el:
                    # print(squares_dict[element], e)
                    if row_dict[element].__contains__(e):
                        row_dict[element][e] += 1
                    else:
                        row_dict[element][e] = 1
    return row_dict


def create_col_dict(platform):
    col_dict = [{} for _ in range(9)]
    for element in platform:
        for el in range(9):
            if type(el) == list:
                for e in element[el]:
                    # print(squares_dict[element], e)
                    if col_dict[el].__contains__(e):
                        col_dict[el][e] += 1
                    else:
                        col_dict[el][e] = 1
    return col_dict


def create_squares(platform):
    squares = list(list([] for i in range(9)) for j in range(9))
    for i in range(3):
        for j in range(0, 9, 3):
            for k in range(3):
                for l in range(3):
                    squares[i * 3 + int(j / 3)][l + k * 3] = platform[k + (j % 3) * 3 + i * 3][l + j]
                    # print(puzzle[k + (j % 3) * 3 + i * 3][l + j], end=" ")
                    # print(i * 3 + int(j / 3), " -", k * 3 + l, end=" ")
    return squares


def delete_incorrect_variable(platform, squares, conundrum):
    row = list(list(conundrum[y][x] for x in range(9) if conundrum[y][x] != 0) for y in range(9))
    col = list(list(conundrum[x][y] for x in range(9) if conundrum[x][y] != 0) for y in range(9))
    for i in range(9):
        for j in range(9):
            if type(platform[i][j]) == int:
                continue
            fishing_elements = set(list(x for x in row[i] + col[j] + list(x for x in squares[i // 3 * 3 + j // 3] if type(x) == int) if x != 0))
            platform[i][j] = list(x for x in platform[i][j] if not x in fishing_elements)


def create_and_filling(conundrum):
    platform = list(
        list(conundrum[y][x] if conundrum[y][x] != 0 else [1, 2, 3, 4, 5, 6, 7, 8, 9] for x in range(9)) for y in
        range(9))
    squares = create_squares(conundrum)

    # Удаление невозможных вариантов
    delete_incorrect_variable(platform, squares, conundrum)

    squares = create_squares(platform)

    return squares, platform


def sudoku_solver(puzzle):
    # Happy Coding!
    # platform = list(list([] for i in range(9)) for j in range(9))
    # row = list(list(puzzle[y][x] if puzzle[y][x] != 0 else [] for x in range(9)) for y in range(9))
    # col = list(list(puzzle[x][y] if puzzle[x][y] != 0 else [] for x in range(9)) for y in range(9))

    # platform = list(list(puzzle[y][x] if puzzle[y][x] != 0 else [] for x in range(9)) for y in range(9))
    squares, platform = create_and_filling(puzzle)
    squares_dict = create_squares_dict(squares)
    row_dict = create_row_dict(platform)
    col_dict = create_col_dict(platform)
    print("\nPlatform")
    for i in platform:
        print(i)

    print("\nSquares")
    for i in squares:
        print(i)

    print("\nSquares_dict")
    for i in squares_dict:
        print(i)

    print("\nRow_dict")
    for i in row_dict:
        print(i)

    print("\nCol_dict")
    for i in col_dict:
        print(i)

    # 1
    for i in range(9):
        for j in range(9):
            if type(platform[i][j]) == list and len(platform[i][j]) == 1:
                platform[i][j] = platform[i][j][0]
    delete_incorrect_variable(platform, squares, puzzle)

    # 2
    print("---------------------------------------------------------")
    for el in squares_dict:
        print(el)

    for element in squares_dict:
        pass

    print("\nPlatform")
    for i in platform:
        print(i)


puzzle = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
          [0, 8, 0, 0, 9, 0, 0, 3, 0],
          [2, 0, 0, 0, 0, 5, 4, 0, 0],
          [4, 0, 0, 0, 0, 1, 8, 0, 0],
          [0, 3, 0, 0, 7, 0, 0, 4, 0],
          [0, 0, 7, 9, 0, 0, 0, 0, 3],
          [0, 0, 8, 4, 0, 0, 0, 0, 6],
          [0, 2, 0, 0, 5, 0, 0, 8, 0],
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]

print("Puzzle")
for i in puzzle:
    print(i)
sudoku_solver(puzzle)

from collections import Counter

mylist = [1, 2, 3, 5, 4, 2]
counter = [k for k, v in Counter(mylist).items() if v > 1]

print(len(counter))