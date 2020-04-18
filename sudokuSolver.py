import numpy as np

class sudokuSolver:

    def __init__(self):
        # Stores the problem statement. This needs to be provided before calling solver.
        self.grid = []

        # Stores all the solutions from solver.
        self.sol = []

# Check if this number is possible to put in this location 
    def possible(self, y, x, n):
        for i in range (0,9):
            if self.grid[y][i] == n:
                return False
        for i in range (0,9):
            if self.grid[i][x] == n:
                return False
        
        x0 = (x//3)*3
        y0 = (y//3)*3

        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y0+i][x0+j] == n:
                    return False
        return True

# Solver to solve for sudoku problem posted
    def solve(self):
        if self.grid == []:
            self.grid = input("Please provide unsolved sudoku grid.\n")

        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y, x, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        self.sol.append(np.matrix(self.grid))

# Print all the solutions found for the problem posted
    def printsol(self):
        i = 0
        print("There is/are "+str(len(self.sol))+" solution.")
        for sol in self.sol:
            i = i+1
            print ("Solution "+str(i)+" :")
            print(sol)

