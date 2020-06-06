# Sudoku Solver
This is a python console program that may show the answer of sudoku problems presented in image files or text file using backtracking algorithm.

## Requirement. 
### Setting Up Pytesseract
1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
2. Note the tesseract path from the installation.Default installation path at the time the time of this edit was: 
'C:/Program Files/Tesseract-OCR/tesseract.exe'. It may change so please check the installation path.
3. ```pip install pytesseract```
4. Set the tesseract path in the script before calling image_to_string:
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
### Setting Up OpenCV
1. ```pip install opencv-python```
### Setting up numpy
1. ```pip install numpy```

## Run
1. Clone this project on your device
2. Change the path in load.py to the path where you installed tesseract.exe 
```pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'```
3. In your project directory run 
```
python run main.py
```
4. An input of the type of file you are going to upload will be requested by integer. Fill with 1 for png file and 2 for txt file.
5. An input of the file's name will be requested.
6. The answer of the sudoku problem and the locations of 5 will be presented in the console and also written in txt file inside the folder result.

## Strategy
This program uses the backtracking algorithm to solve this problem. I personally chose this algorithm because it is the easiest to apply even though it may take a while to get the desired result.
The backtracking algorithm works in sudoku problem by checking whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. 
Time complexity: O(9^(n*n)).
For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)). The time complexity remains the same but there will be some early pruning so the time taken will be much less than the naive algorithm but the upper bound time complexity remains the same to the brute force method.
Space Complexity: O(n*n).
To store the output array a matrix is needed.

## Library
### Tesseract
I chose tesseract for this project because it has the feature that I needed which is transforming an image to a string of number. However, I found a lot of troubles during installation since I made a small mistake with the path written in py file. Not only that, it takes very long for the image to show up and there is a certain warning about the RGB in the console I couldn't get rid of.
### OpenCV
I used opencv to open and read the image and to create the array. I didn't find any trouble using this library.
### Numpy
I used numpy for multidimensional arrays.

## Reference
https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
https://www.geeksforgeeks.org/sudoku-backtracking-7/
https://opencv.org/
https://pypi.org/project/pytesseract/
