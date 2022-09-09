import numpy as np

# generator
print("The following python programme can do the following assessments:")
print("\n- Generate a sudoku(Enter 1) \n- Solve a sudoku(Enter 2) \n- Generate and Solve a sudoku in the same time("
      "Enter 3) \n- Lets you play a "
      "game of sudoku(Enter4)\n\n")
n = int(input("What do u want the programme to do for you?:"))


def gen(difficulty=0.5):
    while True:
        n = 9
        puzzle = np.zeros((n, n), np.int64)
        random = np.arange(1, n + 1)
        puzzle[0, :] = np.random.choice(random, n, replace=False)
        try:
            for r in range(1, n):
                for c in range(n):
                    col_rest = np.setdiff1d(random, puzzle[:r, c])
                    row_rest = np.setdiff1d(random, puzzle[r, :c])

                    uni1 = np.intersect1d(col_rest, row_rest)

                    r_start = (r // 3)
                    c_start = (c // 3)

                    uni2 = np.setdiff1d(np.arange(0, n + 1),
                                        puzzle[r_start * 3:(r_start + 1) * 3, c_start * 3:(c_start + 1) * 3].ravel())

                    uni = np.intersect1d(uni1, uni2)
                    puzzle[r, c] = np.random.choice(uni, size=1)
            break
        except ValueError:
            pass

    puzzle1 = puzzle.copy()
    puzzle1[np.random.choice([True, False], size=puzzle.shape, p=[difficulty, 1 - difficulty])] = 0

    arr = np.array(puzzle1)
    list1 = arr.tolist()

    return list1


board = gen()


def layout(board):
    # for i in range(len(board)):
    #     if i%3==0 and i!=0:
    #             print("--------------------------")

    #     for j in range(len(board[0])):

    #         if j%3==0 and j!=0:
    #                 print("|",end="")

    #         if j==8:
    #             print(board[i][j])

    #         else:
    #             print(str(board[i][j])+" ",end="")

    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("--------------------")

        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                final = (str(board[i][j]))
                print(final.replace('0', " "))

            else:
                final = (str(board[i][j]) + " ")
                print(final.replace('0', " "), end="")


def empty_block(board):
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] == 0:
    #             return(i,j)

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)

    return None


def check(board, sol, row, col):
    # row

    row_val = board[row]
    if sol in row_val:
        return False

        # col

    # col_val=[]
    # for i in range(9):
    #     col_val.append[board[i][col]]
    col_val = [board[i][col] for i in range(9)]
    if sol in col_val:
        return False

    # 3x3 square

    r_start = (row // 3) * 3
    c_start = (col // 3) * 3

    for r in range(r_start, r_start + 3):
        for c in range(c_start, c_start + 3):
            if board[r][c] == sol:
                return False

    return True


def solve(board):
    a = empty_block(board)

    if not a:
        return True

    row, col = a

    for sol in range(1, 10):

        if check(board, sol, row, col):

            board[row][col] = sol

            if solve(board):
                return True

        board[row][col] = 0

    return False


if n == 1:
    layout(board)

elif n == 2:
    sudoku = input("enter your sudoku:")
    print("The Generated sudoku is :\n")
    layout(sudoku)

    if solve(sudoku):
        print("***--------------------***")
        print("The solved sudoku is :\n")
        layout(sudoku)

    else:
        print("not possible")

elif n == 3:
    print("The Generated sudoku is :\n")
    layout(board)

    if solve(board):
        print("***--------------------***")
        print("The solved sudoku is :\n")
        layout(board)

    else:
        print("not possible")

# Game


# if solve(board):
#     print("***--------------------***")
#     layout(board)
# else:
#     print("not possible
