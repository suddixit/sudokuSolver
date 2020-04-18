# Using sudokuSolver Class
from sudokuSolver import sudokuSolver

# Create new object of the class
obj = sudokuSolver()

# Provide 9x9 sudoku problem
obj.grid = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,0,0]]

# Solve the problem for all solutions
obj.solve()

# Print all solutions
obj.printsol()