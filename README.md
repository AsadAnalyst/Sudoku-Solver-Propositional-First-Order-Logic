# 🧠 Sudoku Solver: Propositional & First-Order Logic

> Solve Sudoku puzzles using **Propositional Logic (PL)** and **First-Order Logic (FOL)** side by side, with a visual and educational twist!



## 🔍 Introduction

Sudoku, the classic 9×9 number-placement puzzle, is a perfect problem to demonstrate logical reasoning and constraint satisfaction.  
This project applies **Propositional Logic** and **First-Order Logic** to model and solve Sudoku puzzles through an intuitive **Tkinter-based GUI**.

Explore the power of formal logic and AI as the solver demonstrates:
- Logical constraint encoding
- Side-by-side comparison of PL & FOL results
- Real-time GUI visualization

---

## ✨ Features

- ♟️ **Dual Logic Solvers**  
  Solve puzzles using both Propositional Logic **(PL)** and First-Order Logic **(FOL)**.

- 🖼️ **Graphical User Interface**  
  User-friendly GUI built with Tkinter for puzzle input, editing, and solution visualization.

- 🔎 **Step-by-Step Comparison**  
  Displays both PL and FOL solutions side-by-side for easy analysis.

- ⏱️ **Performance Metrics**  
  Displays time taken and theoretical complexity for both solvers.

- ✏️ **Editable Grid**  
  Users can modify or reset the Sudoku board and solve custom puzzles.

---

## 🧠 Logic Formulations

### ✅ Propositional Logic (PL)

- **Variable Definition:**  
  `X_{r,c,n}` is true if cell (r, c) contains number n

- **Constraints:**
  1. Each cell has **at least one** number  
  2. Each cell has **at most one** number  
  3. Each number appears **once per row**  
  4. Each number appears **once per column**  
  5. Each number appears **once per 3×3 block**

---

### ✅ First-Order Logic (FOL)

- **Predicate:**  
  `Filled(r, c, n)` means cell (r, c) contains number n

- **Constraints:**
  1. Each cell contains **exactly one** number  
  2. Each number appears **once per row**  
  3. Each number appears **once per column**  
  4. Each number appears **once per 3×3 block**

---

## 🛠️ How It Works

1. **Input Grid:**  
   Launches with a default puzzle — you can edit or reset it.

2. **Solve:**  
   Click **"Solve (PL & FOL)"** to begin dual-solving the puzzle.

3. **Visual Output:**  
   - **Original Clues:** Black  
   - **PL Solution:** Blue  
   - **FOL Solution:** Green

4. **Stats:**  
   Time taken and theoretical complexity shown after solving.

---

## 📥 Requirements

- Python 3.x  
- Tkinter (comes pre-installed with Python)

Install additional packages (if any):

```bash
pip install -r requirements.txt
