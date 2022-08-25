
board=[ [2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

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


    for i,row in enumerate(board):
        if i%3==0 and i!=0:
            print("--------------------------")

        for j,val in enumerate(row):
            if j%3==0 and j!=0:
                print("|",end="") 

            if j==8:
                print(board[i][j]) 

            else:
                print(str(board[i][j])+" ",end="")    

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

def check(board,sol,row,col):
    
    #row

    row_val=board[row]
    if sol in row_val:
        return False 
   
    #col

    # col_val=[]
    # for i in range(9):
    #     col_val.append[board[i][col]]
    col_val=[board[i][col] for i in range(9)]
    if sol in col_val:
        return False

    #3x3 square 

    r_start=(row//3)*3
    c_start=(col//3)*3

    for r in range(r_start,r_start+3):
        for c in range(c_start,c_start+3):
            if board[r][c] == sol:
                return False

    return True            

def solve(board):
    a=empty_block(board)

    if not a:
        return True

    row,col=a   

    for sol in range(1,10):

        if check(board,sol,row,col):
            board[row][col]=sol

            if solve(board):
                return True

        board[row][col]=0

    return False

layout(board)
solve(board)
print("--------------------")
layout(board)
