from loader import *
from solver import *
from result import *

if __name__ == '__main__':
    print("Sudoku Solver teretetetet") 
    #Opener jia
    fileType=int(input("Filenya apa? \n1.Gambar\n2.Txt\n "))
    if fileType==2:
        filename=input('text apanii?: (dalam txt ya)\n ')     
        board = loadTxt(filename)  
    elif fileType==1:
        filename=input('gambar apani?: (dalam png + rada lemot sabar ya)\n ')
        board = loadImg(filename)    

    printBoard(board)      
    #printing the board before solving the puzzle
    solve(board)           
    #solving the puzzle
    printBoard(board)      
    #printing the puzzle after solving
    writeAnswer(board, filename)
    #writing the answer in txt
    print("Where are the 5:")
    print(findFive(board))
    #print out the location of 5s
