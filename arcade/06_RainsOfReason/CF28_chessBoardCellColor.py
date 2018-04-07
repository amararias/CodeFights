# Given two cells on the standard chess board, determine whether they have the same color or not.

# Example

# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.

def whiteOrBlack(cell):
    # returns True if is BLACK, False otherwise
    row = int(cell[-1])
    col = ord(cell[0].upper())
    
    return True if row%2 == col%2 else False

def chessBoardCellColor(cell1, cell2):
    return whiteOrBlack(cell1) == whiteOrBlack(cell2)

cell1 = "A1" 
cell2 = "H3"
print(chessBoardCellColor(cell1, cell2))