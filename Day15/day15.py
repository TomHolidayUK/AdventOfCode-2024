data_path = './day15_data.txt'

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


# Find sum
def sum(grid):
    sum = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "O" or char == "[":
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


rows, cols = len(scaled_grid), len(scaled_grid[0])

def move2(scaled_grid, instruction):
    # find fish
    fish = 0, 0
    for y, line in enumerate(scaled_grid):
        for x, char in enumerate(line):
            if char == "@":
                fish = x, y

    # move in direction of instruction
    next_x, next_y = next_positions(fish, instruction)

    # if at edge
    if scaled_grid[next_y][next_x] == "#":
        #print("at edge, no move")
        return scaled_grid

    # if wall
    if scaled_grid[next_y][next_x] == "[" or scaled_grid[next_y][next_x] == "]":
        # laterally, the same logic as part 1 applies
        if instruction == "<" or instruction == ">":
            #print("lateral wall movement, same as part 1")
            while scaled_grid[next_y][next_x] == "[" or scaled_grid[next_y][next_x] == "]":
                next_x, next_y = next_positions([next_x, next_y], instruction)
            if scaled_grid[next_y][next_x] == "#":
                #print("walls against the edge, don't move")
                return scaled_grid
            if scaled_grid[next_y][next_x] == ".":
                #print("need to move wall(s)")
                scaled_grid = change_grid(scaled_grid, fish, ".")
                next_fish = next_positions(fish, instruction)
                scaled_grid = change_grid(scaled_grid, next_fish, "@")
                # need to change all the walls in between:
                for i in range(2, abs(next_x - fish[0]) + 1):
                    if instruction == "<":
                        temp_x = fish[0] - i
                    if instruction == ">":
                        temp_x = fish[0] + i
                    if i % 2 == 0:
                        if instruction == ">":
                            scaled_grid = change_grid(scaled_grid, [temp_x, fish[1]], "[")
                        if instruction == "<":
                            scaled_grid = change_grid(scaled_grid, [temp_x, fish[1]], "]")
                    if i % 2 != 0:
                        if instruction == ">":
                            scaled_grid = change_grid(scaled_grid, [temp_x, fish[1]], "]")
                        if instruction == "<":
                            scaled_grid = change_grid(scaled_grid, [temp_x, fish[1]], "[")
                return scaled_grid


        group = set()

        #print("potentially need to move walls vertically")
        should_continue = True
        gs_x, gs_y = next_x, next_y # group search location
        group.add((gs_x, gs_y, scaled_grid[gs_y][gs_x]))
        next_row = []
        next_row.append([gs_x, gs_y])
        space = True
        while should_continue == True:

            current_row = []
            # append other halfs of walls to group
            for cell in next_row:
                if cell not in current_row:
                    current_row.append(cell)
                    group.add((cell[0], cell[1], scaled_grid[cell[1]][cell[0]]))
                if scaled_grid[cell[1]][cell[0]] == "]" and [cell[0] - 1, cell[1]] not in current_row:
                    group.add((cell[0] - 1, cell[1], scaled_grid[cell[1]][cell[0] - 1]))
                    current_row.append([cell[0] - 1, cell[1]])
                if scaled_grid[cell[1]][cell[0]] == "[" and [cell[0] + 1, cell[1]] not in current_row:
                    group.add((cell[0] + 1, cell[1], scaled_grid[cell[1]][cell[0] + 1]))
                    current_row.append([cell[0] + 1, cell[1]])

            next_row = []

            # once we have all the walls, search upwards on current row
            for cell in current_row:
                if instruction == "^":
                    if (scaled_grid[cell[1] - 1][cell[0]] == "]" or scaled_grid[cell[1] - 1][cell[0]] == "["):
                        next_row.append([cell[0], cell[1] - 1])
                    if scaled_grid[cell[1] - 1][cell[0]] == "#":
                        #print("can't move walls")
                        return scaled_grid
                if instruction == "v":
                    if (scaled_grid[cell[1] + 1][cell[0]] == "]" or scaled_grid[cell[1] + 1][cell[0]] == "["):
                        next_row.append([cell[0], cell[1] + 1])
                    if scaled_grid[cell[1] + 1][cell[0]] == "#":
                        #print("can't move walls")
                        return scaled_grid

            if len(next_row) == 0:
                #print("stop")
                should_continue = False
                break
            else:
                # go to next row
                gs_x, gs_y = next_row[0][0], next_row[0][1]
            
        
        # then check if there is space for them to move
        if len(group) > 0:
            #print("need to move group of ", len(group))
            new_group = []
            old_group = []
            for char in group:
                    if instruction == "^":
                        new_group.append([char[0], char[1] - 1])
                    if instruction == "v":
                        new_group.append([char[0], char[1] + 1])
                    old_group.append([char[0], char[1]])

            # if there is space, move them
            if space:
                if instruction == "^":
                    # change chars in group
                    for char in group:
                        scaled_grid = change_grid(scaled_grid, [char[0], char[1] - 1], char[2])

                        # and the chars that trail the group when it moves
                        if [char[0], char[1]] in old_group and [char[0], char[1]] not in new_group:
                            scaled_grid = change_grid(scaled_grid, [char[0], char[1]], ".")

                if instruction == "v":
                    for char in group:
                        scaled_grid = change_grid(scaled_grid, [char[0], char[1] + 1], char[2])

                        if [char[0], char[1]] in old_group and [char[0], char[1]] not in new_group:
                            scaled_grid = change_grid(scaled_grid, [char[0], char[1]], ".")

                scaled_grid = change_grid(scaled_grid, [next_x, next_y], "@")
                scaled_grid = change_grid(scaled_grid, [fish[0], fish[1]], ".")

                return scaled_grid
        else:
            #print("ERROR - can't move group")
            return scaled_grid

            

    
    # if space 
    if scaled_grid[next_y][next_x] == ".":
        #print("space so moving")
        scaled_grid = change_grid(scaled_grid, fish, ".")
        scaled_grid = change_grid(scaled_grid, [next_x, next_y], "@")
        return scaled_grid

f = 0
for instruction in instructions:
    if (instruction != "\n"):
        scaled_grid = move2(scaled_grid, instruction)
        f += 1

# print('\n'.join(scaled_grid))

print("Part 2 Result = ", sum(scaled_grid))
