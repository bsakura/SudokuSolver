
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
    return None
    
def valid(board, num, pos):
    row = pos[0]
    column = pos[1]
    #checking rows
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    #checking columns
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False   
    #checking box
    startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

def solve(board):
    find = findEmpty(board)    
    if not find:
        return True
    else:
        row, col = find   
    for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i           
            if solve(board):
                return True           
            board[row][col] = 0
    return False
