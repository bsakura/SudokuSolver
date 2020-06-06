import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def loadTxt(filename):
    board = []
    name = filename.split('/')
    fileHandle = open("../test/"+name[-1], "r")
    puzzle = fileHandle.readlines()
    for line in range(len(puzzle)):
        if line != len(puzzle) - 1:
            puzzle[line]=puzzle[line].replace('#','0')
            puzzle[line] = puzzle[line][:-1]
            board.append(list(map(int,puzzle[line].split(" "))))
        else:
            puzzle[line]=puzzle[line].replace('#','0')
            board.append(list(map(int,puzzle[line].split(" "))))
    fileHandle.close()
    return board

def loadImg(filename):
    name = filename.split('/')
    im = cv2.resize(cv2.imread("../test/"+name[-1]), (900, 900))
    out = np.zeros((9, 9), dtype=np.uint8)
    for x in range(9):
        for y in range(9):
            num = pytesseract.image_to_string(im[10 + x*100:(x+1)*100 - 10, 10 + y*100:(y+1)*100 - 10, :], config='--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789')
            if num:
                out[x, y] = num
    return out
