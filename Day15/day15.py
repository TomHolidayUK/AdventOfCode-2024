data_path = './day15_data_test3.txt'

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

rows, cols = len(scaled_grid), len(scaled_grid[0])

# def dfs(grid, x, y, visited):
#         # the coordinate convention is swapped in this function!!! - taken from Day 10
#         print("current pos: ", x, y)

#         # avoid repetition
#         if (x,y) in in_group:
#             return

#         group.append([x,y])
              
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
#         for dx, dy in directions:
#             new_x, new_y = x + dx, y + dy

#             if 0 <= new_x < rows and 0 <= new_y < cols and not visited[new_y][new_x] and grid[new_y][new_x] == "[" or grid[new_y][new_x] == "]" :
#                 visited[new_y][new_x] = True
                
#                 # Recurse to continue exploring
#                 dfs(new_x, new_y, visited, group_number)

#                 # add conjoing part of wall
#                 if grid[y][x] == "[":
#                     group.append([x + 1,y])
#                 if grid[y][x] == "]":
#                     group.append([x - 1,y])

#                 # after exploring all possible paths from current cell mark as not visited so it can be included in other paths
#                 # this essentially allows backtracking
#                 visited[new_y][new_x] = False


def move2(grid, instruction):
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
        print("at edge, no move")
        return grid

    # if wall
    if grid[next_y][next_x] == "[" or grid[next_y][next_x] == "]":

        # laterally, the same logic as part 1 applies
        if instruction == "<" or instruction == ">":
            print("lateral wall movement, same as part 1")
            while grid[next_y][next_x] == "[" or grid[next_y][next_x] == "]":
                next_x, next_y = next_positions([next_x, next_y], instruction)
            if grid[next_y][next_x] == "#":
                print("walls against the edge, don't move")
                return grid
            if grid[next_y][next_x] == ".":
                print("need to move wall(s)")
                grid = change_grid(grid, fish, ".")
                next_fish = next_positions(fish, instruction)
                grid = change_grid(grid, next_fish, "@")
                # need to change all the walls in between:
                print("index = ", next_x - fish[0])
                for i in range(next_x - fish[0]):
                    print(i)
                    temp_x = fish[0] + i
                    if grid[temp_x][fish[1]] == "[":
                        grid = change_grid(grid, [ftemp_x, fish[1]], "]")
                    if grid[temp_x][fish[1]] == "]":
                        grid = change_grid(grid, [ftemp_x, fish[1]], "[")
                return grid


        # apply DFS to find all walls that could move 
        group = []
        # visited = [[False] * cols for _ in range(rows)]  # 2D array to track visited cells
        # visited[0][0] = True  # Mark the start as visited
        # dfs(scaled_grid, next_y, next_x, visited)

        should_continue = True
        gs_x, gs_y = next_x, next_y # group search location
        group.append([gs_x, gs_y])
        next_row = []
        next_row.append([gs_x, gs_y])
        while should_continue == True:
            current_row = []
            current_row.append([gs_x, gs_y])
            # append other halfs of walls to group
            for cell in next_row:
                if grid[gs_y][gs_x] == "]" and [gs_x - 1, gs_y] not in group:
                    group.append([gs_x - 1, gs_y])
                    current_row.append([gs_x - 1, gs_y])
                if grid[gs_y][gs_x] == "[" and [gs_x + 1, gs_y] not in group:
                    group.append([gs_x + 1, gs_y])
                    current_row.append([gs_x + 1, gs_y])

            next_row = []

            # once we have all the walls, search upwards on current row
            for cell in current_row:
                if (grid[cell[0]][cell[1] - 1] == "]" or grid[cell[0]][cell[1] - 1] == "["):
                    next_row.append([cell[0]][cell[1] - 1])
                if grid[cell[0]][cell[1] - 1] == "#":
                    print("can't move walls")
                    group = []
                    break

            if len(next_row) == 0:
                print("stop")
                should_continue = False

        # then check if there is space for them to move

        # if there is space, move them

    # if space 
    if grid[next_y][next_x] == ".":
        print("space so moving")
        grid = change_grid(grid, fish, ".")
        grid = change_grid(grid, [next_x, next_y], "@")
        return grid







print(move2(scaled_grid, "<"))