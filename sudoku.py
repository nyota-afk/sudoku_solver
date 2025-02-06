# -*- coding: utf-8 -*-
"""
Sudoku solver

@author: lisa
"""

def solve_sudoku(puzzle):
    """
    solves sudoku using backtracking
    returns True if the sudiku is solved
    returns False if the sudoku is unsolvable 
    """
    # 1. find next empty cell
    empty_cell = next_empty_cell(puzzle)
    if not empty_cell:
        return True # the puzzle is full/solved
    # 2. try numbers 1-9 and check if the entry is valid
    row, col = empty_cell
    for num in range(1,10):
        if is_valid(puzzle, num, row, col):
            # 3. temporary note number and recursively use solve sudoku to check for conflicts
            puzzle[row][col] = num
            
            if solve_sudoku(puzzle):
                return True  
            
            # 4. if a confict occurs use backtracking
            puzzle[row][col] = 0
   
    # final step return true if soduku is solved and false if the puzzle is unsolvable
    return False
    
def next_empty_cell(puzzle):
    # finds next empty cell in the puzzle, returns location as tuple
    # returns (none) if the puzzle is filled
    
    #step 1: find next empty space to make a guess
    for r in range(9):      # go through all 9 rows
        for c in range(9):  # go through all 9 cells 
            if puzzle[r][c] == 0:
                return (r,c)
    return None
            
def is_valid(puzzle, num, row, col):
    
    # check if number is valid for column and row
    # check row 
    if num in puzzle[row]: 
        return False
    
    # check column
    if num in [puzzle[i][col] for i in range(9)]:
        return False
    
    # check 3x3 block
    """
    calculate the starting point for each block
     (0,0)   (0,3)   (0,6)
     (3,0)   (3,3)   (3,6)
     (6,0)   (6,3)   (6,6)
     """
    block_row = (row // 3) * 3
    block_col = (col // 3) * 3
    # searches number in 3x3 block
    for r in range(3):
        for c in range(3):
            if puzzle[block_row + r][block_col + c] == num:
                return False
    return True

#print((5 // 3) *3)
#print((2 //3) * 3)