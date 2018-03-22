# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

# Example

# For

# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
# the output should be

# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]] 

import numpy as np

def extractSurroundingMatrix(matrix, r, c):
    result = matrix[r, c]
    indices = [r-1, r+1, c-1, c+1]
    for pos, index in enumerate(indices):
        if index < 0:
            index = 0
        elif index > matrix.shape[0]:
            index = matrix.shape[0]
        indices[pos] = index

    r_i, r_f, c_i, c_f = indices 

    if result == True:
        return np.sum(matrix[r_i:r_f+1, c_i:c_f+1]) - 1
    else:
        return np.sum(matrix[r_i:r_f+1, c_i:c_f+1]) 
    

def minesweeper(matrix):
    Y = np.array(matrix, dtype=np.bool)
    rows, cols = Y.shape
    output = []
    for row in range(rows):
        output_row = []
        for col in range(cols):
            output_row.append(
                extractSurroundingMatrix(Y,row,col)
                )
        output.append(output_row)
    return output

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]

print(minesweeper(matrix))