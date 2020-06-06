from solver import *

def findFive(board):
    nodes = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 5:
                nodes.append((j+1, i+1)) #row, column
    return nodes

def printBoard(board):
    if not findEmpty(board):
        print("Finished puzzle")
    else:
        print("Unsolved puzzle")
    for i in range(len(board)):
        if i%3 == 0:
            print("-------------------")
            
        for j in range(len(board[0])):
            if j%3 == 0:
                print("\b|", end ="")
            
            print(str(board[i][j])+" ", end="")
        print("\b|")
    print("-------------------")
        

def writeAnswer(board,filename):
        name = filename.split('/')
        f = open("../result/"+name[-1]+".txt",'w')
        print("Result Sudoku Teretetetetetet",file=f)
        for j,lines in enumerate(board):
            for i,num in enumerate(lines):
                print(num,end=" ",file=f)
                if i % 3 == 2 and i != 8:
                    print('|',end="",file=f) 
            print("",file=f)
            if j % 3 == 2 and j != 8:
                print('--------------------',file=f)
        print("Where are the 5 : ",end="",file=f)
        for i in range(9):
            for j in range(9):
                if board[i][j] == 5:
                    print(f"({i},{j})",end=" ",file=f)
        f.close()
