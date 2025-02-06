import tkinter as tk
from tkinter import Canvas
import time
from sudoku import next_empty_cell, is_valid

def draw_grid(canvas):
    for i in range(10):
        width = 3 if i % 3 == 0 else 1
        canvas.create_line(50 + i * 50, 50, 50 + i * 50, 500, width=width)
        canvas.create_line(50, 50 + i * 50, 500, 50 + i * 50, width=width)

def draw_numbers(canvas, puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != 0:
                canvas.create_text(75 + j * 50, 75 + i * 50, text=str(puzzle[i][j]), font=("Arial", 18))

def solve_sudoku_gui(canvas, puzzle):
    empty_cell = next_empty_cell(puzzle)
    if not empty_cell:
        return True
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(puzzle, num, row, col):
            puzzle[row][col] = num
            canvas.create_text(75 + col * 50, 75 + row * 50, text=str(num), font=("Arial", 18), fill='blue')
            canvas.update()
            time.sleep(0.1)
            
            if solve_sudoku_gui(canvas, puzzle):
                return True
            
            puzzle[row][col] = 0
            canvas.create_rectangle(50 + col * 50 + 5, 50 + row * 50 + 5, 50 + (col+1) * 50 - 5, 50 + (row+1) * 50 - 5, fill="white", outline="white")
            canvas.update()
            time.sleep(0.1)
    
    return False


def main():
    root = tk.Tk()
    root.title("Sudoku Solver")
    canvas = Canvas(root, width=550, height=550)
    canvas.pack()
    
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    draw_grid(canvas)
    draw_numbers(canvas, puzzle)
    root.update()
    
    root.after(500, lambda: solve_sudoku_gui(canvas, puzzle))
    root.mainloop()

if __name__ == "__main__":
    main()
