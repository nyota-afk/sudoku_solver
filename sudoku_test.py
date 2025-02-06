import unittest
import time
from sudoku import solve_sudoku, is_valid, next_empty_cell

class TestSudokuSolver(unittest.TestCase):

    def setUp(self):
        # Set up a Sudoku puzzle for testing
        self.puzzle = [
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

    def test_solve_sudoku(self):
        #Testet, ob das Sudoku korrekt gelöst wird
        self.assertTrue(solve_sudoku(self.puzzle))
        for row in self.puzzle:
            self.assertNotIn(0, row)  # Es sollten keine leeren Zellen (0) mehr vorhanden sein

    def test_next_empty_cell(self):
        #Testet, ob die nächste leere Zelle gefunden wird."""
        self.assertEqual(next_empty_cell(self.puzzle), (0, 2))  # Erste leere Zelle sollte an (0,2) sein

    def test_is_valid(self):
        #Testet die Gültigkeitsprüfung von Zahlen."""
        self.assertTrue(is_valid(self.puzzle, 4, 0, 2))  # 4 sollte an (0,2) erlaubt sein
        self.assertFalse(is_valid(self.puzzle, 3, 0, 2))  # 3 ist schon in der Zeile, sollte nicht erlaubt sein

    def test_performance_solve(self):
        #Misst die Laufzeit des Sudoku-Solvers
        start_time = time.time()
        solve_sudoku(self.puzzle)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Laufzeit für Sudoku-Lösung: {elapsed_time:.6f} Sekunden")
        self.assertLess(elapsed_time, 1)  # Erwartet, dass die Lösung in unter 1 Sekunde liegt

    def test_unsolvable_puzzle(self):
        # tries a puzzle that is unsolvable
        self.puzzle = [
            [5, 3, 0, 7, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.assertFalse(solve_sudoku(self.puzzle))
        
    def test_performance_hard_puzzle(self):
        # speed test with a hard sudoku puzzle
        self.puzzle = [
            [0, 0, 8, 0, 0, 5, 3, 0, 0],
            [0, 0, 6, 0, 0, 2, 0, 0, 7],
            [0, 0, 0, 0, 9, 0, 0, 8, 0],
            [0, 4, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 9, 8, 0, 0, 0, 0],
            [8, 0, 0, 6, 0, 3, 0, 4, 0],
            [0, 0, 5, 0, 2, 0, 0, 6, 0],
            [9, 0, 0, 3, 0, 0, 4, 0, 5],
            [0, 7, 0, 0, 0, 0, 9, 0, 0]
            ]
        start_time = time.time()
        solve_sudoku(self.puzzle)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Laufzeit für schweres Sudoku-Lösung: {elapsed_time:.6f} Sekunden")

if __name__ == "__main__":
    unittest.main()
