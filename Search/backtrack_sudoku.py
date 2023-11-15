def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if grid[i][j] == num:
                return False

    return True

def add_to_led_to_backtracking_dict(row, col, num, led_to_backtracking_dict): #I am assuming this changes the dictionary in place as a C reference would
    cur_val = led_to_backtracking_dict.get((row,col))
    if cur_val == None: led_to_backtracking_dict[(row,col)] = [num]
    else: led_to_backtracking_dict[(row,col)].append(num)

def back_one_step(row, col):
    if col == 0:
        col, row = 4, row-1
    else:
        col-=1
    return (row,col)

def next_step(row, col):
    if col == 3:
        col, row = 0, row+1
    else:
        col+=1
    return (row,col)

def backtrack(grid, nonmodifiable_squares,led_to_backtracking_dict, row, col):
    if col == 0 and row == 0: raise Exception("No solution!")
    grid[row][col] = 0
    cur_square = back_one_step(row, col)
    while (cur_square in nonmodifiable_squares):
        row, col = cur_square[0], cur_square[1]
        cur_square = back_one_step(row, col)
    row,col = cur_square
    add_to_led_to_backtracking_dict(row,col,grid[row][col],led_to_backtracking_dict)
    vals = [1,2,3,4]
    not_permissible = led_to_backtracking_dict[(row,col)]
    permissible_vals = [x for x in vals if x not in not_permissible]
    for num in permissible_vals:
        if is_valid_move(grid, row, col, num): 
            grid[row][col] = num
            ret = (row,col)
            return ret
    #solution not found and we have to backtrack further: then we have to delete theprohibited values and call the backtrack function again
    led_to_backtracking_dict.popitem() #think this should pop the (row,col) item we are currently at
    return backtrack(grid, nonmodifiable_squares,led_to_backtracking_dict, row, col)


def solve_sudoku(grid):
    #the tuples represent (row, column)
    nonmodifiable_squares = []
    for row in range(4):
        for col in range(4):
            if grid[row][col] != 0:
                nonmodifiable_squares.append((row,col))
    
    led_to_backtracking_dict = {
    #values are in form: (row, column): [values that were tried and led to backtracking]
    }


    row = 0
    col = 0
    while(row<4):
        if grid[row][col]==0:
            for num in [1,2,3,4]:
                if is_valid_move(grid, row, col, num): 
                    grid[row][col] = num
                    break
            if grid[row][col]==0: #this means that we did not find a satisfying value => backtrack
                row,col = backtrack(grid, nonmodifiable_squares,led_to_backtracking_dict, row, col)
        row, col = next_step(row, col)


    return True

sudoku_grid1 = [
    [0, 0, 0, 2],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 3, 0]
]

sudoku_grid2 = [
    [2, 0, 0, 0],
    [0, 0, 0, 4],
    [3, 0, 0, 0],
    [0, 0, 0, 1]
]

sudoku_grid3 = [
    [0, 0, 0, 0],
    [1, 3, 0, 0],
    [0, 0, 4, 1],
    [0, 0, 0, 0]
]

print("Sudoku puzzle 1:")
print_grid(sudoku_grid1)

if solve_sudoku(sudoku_grid1):
    print("Solved Sudoku:")
    print_grid(sudoku_grid1)
else:
    print("No solution exists.")

print("Sudoku puzzle 2:")
print_grid(sudoku_grid2)

if solve_sudoku(sudoku_grid2):
    print("Solved Sudoku:")
    print_grid(sudoku_grid2)
else:
    print("No solution exists.")

print("Sudoku puzzle 3:")
print_grid(sudoku_grid3)

if solve_sudoku(sudoku_grid3):
    print("Solved Sudoku:")
    print_grid(sudoku_grid3)
else:
    print("No solution exists.")

