data_path = './day15_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Plan
# Split data into grid and intructions
# Create a move function that accounts for moving blocks and returns the new grid
# Apply the move function for all instructions
# Find sum


# Split data into grid and intructions
matrix, instructions = file_content.split('\n\n')
grid = matrix.split('\n')

# Create a move function that accounts for moving blocks and returns the new grid

def next_positions(position, instruction):
    x, y = position[0], position[1]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
    direction = None
    if instruction == "^":
        direction = 3
    if instruction == ">":
        direction = 0   
    if instruction == "v":
        direction = 2
    if instruction == "<":
        direction = 1 

    dx, dy = directions[direction][0], directions[direction][1]
    next_x, next_y = x + dx, y + dy
    return [next_x, next_y]

def change_grid(position, new_state):
    # we need a function to change the grid 

def move(grid, instruction):
    # find fish
    fish = 0, 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                fish = x, y

    # move in direction of instruction
    next_x, next_y = next_positions(fish, instruction)
    print("next position = ", next_x, next_y)

    # if at edge
    if grid[next_y][next_x] == "#":
        print("at edge, no move")
        return
    
    # if wall
    if grid[next_y][next_x] == "0":
        # check if it can move
        while grid[next_y][next_x] == "0":
            next_x, next_y = next_positions([next_x, next_y], instruction)
        if grid[next_y][next_x] == "#":
            print("walls against the edge, don't move")
        if grid[next_y][next_x] == ".":
            print("need to move walls")

    # if space 
    if grid[next_y][next_x] == ".":
        print("space so moving")
        grid[y][x] == "."
        grid[next_y][next_x] == "@"
        return grid


print(move(grid, "^"))
matrix[20] = "."
print(matrix[20])


