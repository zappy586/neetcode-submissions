import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # run 3 for loops, one for each - row, column, 3x3 grid
        # check for duplicates. If there is one found, exit the loop and return false
        # Else return true
        digit_to_coord = {}
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value == '.':
                    continue
                if digit_to_coord.get(value) is None:
                    digit_to_coord[value] = [(row,col)]
                else:
                    digit_to_coord[value].append((row, col))

        for i in digit_to_coord.keys():
            coords = digit_to_coord[i]
            rows = []
            cols = []
            grids = []
            for row, col in coords:
                print(rows, cols, grids)
                print(row, col)
                grid_row = int(row/3)
                grid_col = int(col/3)
                if row in rows or col in cols or (grid_row, grid_col) in grids:
                    return False
                else:
                    rows.append(row)
                    cols.append(col)
                    grids.append((grid_row, grid_col))

        return True
                

                # [4, 5] -> int(1/3) = 1; int(5/3) = 1; 0+1 = 1