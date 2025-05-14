aimport tkinter as tk
from tkinter import messagebox
import copy
import time

def is_valid(board, row, col, num):
    # Check if num is not in the current row
    if num in board[row]:
        return False
    # Check if num is not in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if num is not in the current 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_fol(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_fol(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def solve_pl(grid):
    def is_valid_pl(board, row, col, num):
        # Each number appears exactly once in each row
        if num in board[row]:
            return False
        # Each number appears exactly once in each column
        for i in range(9):
            if board[i][col] == num:
                return False
        # Each number appears exactly once in each 3x3 block
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_pl(grid, row, col, num):
                        grid[row][col] = num
                        if solve_pl(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver - PL & FOL")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.initial_grid = [
            [0, 0, 0, 0, 4, 0, 0, 5, 0],
            [4, 0, 7, 0, 0, 0, 6, 0, 2],
            [8, 2, 0, 6, 0, 0, 0, 7, 4],
            [0, 0, 0, 0, 1, 0, 5, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 4, 0, 5, 0, 0, 0, 0],
            [9, 6, 0, 0, 0, 3, 0, 4, 5],
            [3, 0, 5, 0, 0, 0, 8, 0, 1],
            [0, 7, 0, 0, 2, 0, 0, 3, 0]
        ]
        self.create_widgets()

    def create_widgets(self):
        # Input grid
        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=0, column=0, columnspan=2, pady=10)
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.input_frame, width=2, font=('Arial', 16), justify='center')
                e.grid(row=i, column=j, padx=1, pady=1)
                val = self.initial_grid[i][j]
                if val != 0:
                    e.insert(0, str(val))
                    e.config(fg='black', state='disabled')
                self.entries[i][j] = e
        tk.Label(self.input_frame, text="Input Grid", font=('Arial', 12, 'bold')).grid(row=0, column=10, rowspan=2, padx=10)

        # Solution frames
        self.pl_frame = tk.Frame(self.root, bd=2, relief='groove')
        self.fol_frame = tk.Frame(self.root, bd=2, relief='groove')
        self.pl_frame.grid(row=1, column=0, padx=10, pady=5)
        self.fol_frame.grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.pl_frame, text="PL Solution", font=('Arial', 12, 'bold'), fg='blue').grid(row=0, column=0, columnspan=9)
        tk.Label(self.fol_frame, text="FOL Solution", font=('Arial', 12, 'bold'), fg='green').grid(row=0, column=0, columnspan=9)
        self.pl_cells = [[None for _ in range(9)] for _ in range(9)]
        self.fol_cells = [[None for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                pl_lbl = tk.Label(self.pl_frame, width=2, height=1, font=('Arial', 16), borderwidth=1, relief='solid', bg='white')
                pl_lbl.grid(row=i+1, column=j, padx=1, pady=1)
                self.pl_cells[i][j] = pl_lbl
                fol_lbl = tk.Label(self.fol_frame, width=2, height=1, font=('Arial', 16), borderwidth=1, relief='solid', bg='white')
                fol_lbl.grid(row=i+1, column=j, padx=1, pady=1)
                self.fol_cells[i][j] = fol_lbl
        self.pl_time_label = tk.Label(self.pl_frame, text="", font=('Arial', 10))
        self.pl_time_label.grid(row=11, column=0, columnspan=9)
        self.fol_time_label = tk.Label(self.fol_frame, text="", font=('Arial', 10))
        self.fol_time_label.grid(row=11, column=0, columnspan=9)

        # Buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self.button_frame, text="Solve (PL & FOL)", command=self.solve_both, font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10)
        tk.Button(self.button_frame, text="Reset", command=self.reset, font=('Arial', 12)).grid(row=0, column=1, padx=10)
        tk.Button(self.button_frame, text="Edit Input", command=self.enable_edit, font=('Arial', 12)).grid(row=0, column=2, padx=10)

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def display_solutions(self, pl_grid, fol_grid, clues):
        for i in range(9):
            for j in range(9):
                # PL
                if clues[i][j] != 0:
                    self.pl_cells[i][j].config(text=str(clues[i][j]), fg='black', bg='white')
                else:
                    self.pl_cells[i][j].config(text=str(pl_grid[i][j]), fg='blue', bg='white')
                # FOL
                if clues[i][j] != 0:
                    self.fol_cells[i][j].config(text=str(clues[i][j]), fg='black', bg='white')
                else:
                    self.fol_cells[i][j].config(text=str(fol_grid[i][j]), fg='green', bg='white')

    def solve_both(self):
        grid = self.get_grid()
        clues = copy.deepcopy(grid)
        # PL
        pl_start = time.time()
        pl_grid = copy.deepcopy(grid)
        pl_solved = solve_pl(pl_grid)
        pl_time = time.time() - pl_start
        # FOL
        fol_start = time.time()
        fol_grid = copy.deepcopy(grid)
        fol_solved = solve_fol(fol_grid)
        fol_time = time.time() - fol_start
        if pl_solved and fol_solved:
            self.display_solutions(pl_grid, fol_grid, clues)
            self.pl_time_label.config(text=f"Time: {pl_time:.3f}s | Complexity: O(9^(n^2))")
            self.fol_time_label.config(text=f"Time: {fol_time:.3f}s | Complexity: O(9^(n^2))")
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].config(state='disabled')
        else:
            if not pl_solved:
                messagebox.showerror("Error", "No solution found using Propositional Logic (PL).")
            if not fol_solved:
                messagebox.showerror("Error", "No solution found using First-Order Logic (FOL).")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state='normal')
                self.entries[i][j].delete(0, tk.END)
                val = self.initial_grid[i][j]
                if val != 0:
                    self.entries[i][j].insert(0, str(val))
                    self.entries[i][j].config(fg='black', state='disabled')
                else:
                    self.entries[i][j].config(fg='black')
        for i in range(9):
            for j in range(9):
                self.pl_cells[i][j].config(text="", bg='white')
                self.fol_cells[i][j].config(text="", bg='white')
        self.pl_time_label.config(text="")
        self.fol_time_label.config(text="")
        for widget in self.input_frame.grid_slaves():
            if isinstance(widget, tk.Label) and widget.cget('text').startswith('Input Grid'):
                widget.config(text='Input Grid')

    def enable_edit(self):
        # Enable all input cells for editing (including original clues)
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state='normal', fg='black')
        # Update the label to reflect that the grid is now editable
        for widget in self.input_frame.grid_slaves():
            if isinstance(widget, tk.Label) and widget.cget('text').startswith('Input Grid'):
                widget.config(text='Input Grid (Editable)')
        # Clear solution grids and timing labels
        for i in range(9):
            for j in range(9):
                self.pl_cells[i][j].config(text="", bg='white')
                self.fol_cells[i][j].config(text="", bg='white')
        self.pl_time_label.config(text="")
        self.fol_time_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
