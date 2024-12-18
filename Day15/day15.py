data_path = './day15_data_test2.txt'

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
start_grid = grid[:]

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

def change_grid(grid, position, new_state):
    # we need a function to change the grid 
    x, y = position[0], position[1]
    grid[y] = grid[y][:x] + new_state + grid[y][x+1:]
    return grid


def move(grid, instruction):
    # find fish
    fish = 0, 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "@":
                fish = x, y

    # move in direction of instruction
    next_x, next_y = next_positions(fish, instruction)

    # if at edge
    if grid[next_y][next_x] == "#":
        #print("at edge, no move")
        return grid

    # if wall
    if grid[next_y][next_x] == "O":
        # check if it can move
        moves = 0 
        while grid[next_y][next_x] == "O":
            next_x, next_y = next_positions([next_x, next_y], instruction)
            moves += 1
        if grid[next_y][next_x] == "#":
            #print("walls against the edge, don't move")
            return grid
        if grid[next_y][next_x] == ".":
            #print("need to move wall(s)")
            # only start and end of wall chain change stat
            grid = change_grid(grid, fish, ".")
            grid = change_grid(grid, [next_x, next_y], "O")
            next_fish = next_positions(fish, instruction)
            grid = change_grid(grid, next_fish, "@")
            return grid

    # if space 
    if grid[next_y][next_x] == ".":
        #print("space so moving")
        grid = change_grid(grid, fish, ".")
        grid = change_grid(grid, [next_x, next_y], "@")
        return grid


# Apply the move function for all instructions
for instruction in instructions:
    if (instruction != "\n"):
        grid = move(grid, instruction)

print(grid)

# Find sum
def sum(grid):
    sum = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "O":
                sum += (100 * y) + x
    return sum 

print("Part 1 Result = ", sum(grid))
      
# Part 2 Plan
# Scale up grid
# Update move() to account for changes, need to:
#       - find all boxes that will be moved (use DFS???)
#       - calculate new grid arrangement
# Run on all instructions and find sum

# Scale up grid
grid = start_grid
print(grid)

scaled_grid = []

for line in grid:
    scaled_line = ""
    for char in line:
        if char == "#":
            scaled_line += "##"
        if char == ".":
            scaled_line += ".."
        if char == "O":
            scaled_line += "[]"
        if char == "@":
            scaled_line += "@."
    scaled_grid.append(scaled_line)

print(scaled_grid)



