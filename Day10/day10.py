data_path = './day10_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = []

for line in file_content.split('\n'):
    if line: 
        row = [int(char) if char != '.' else '.' for char in line]
        grid.append(row)


#PLAN
# 1 - find every trailhead
# 2 - for every trailhead find the number of paths
#     we need to use a depth first search to find all paths 
#     this will go down all possible paths, recording visited squares
#     once we get to an end (either the end of a trail or a deadend) we backtrack


# 1 
trailheads = []
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 0:
            trailheads.append([y,x])

# 2
# dfs function (depth first search)
# return if reached the goal (and add to total number of paths)
# look in every direction to see if there are any possible directions that haven't been visited
# if there are, move there and add to visited
# then recursively call again
# if no possible path found, backtrack by going back in the current path

rows, cols = len(grid), len(grid[0])

def dfs(grid, y, x, visited):
        global trailhead_total
        current_value = grid[y][x]
        print("current position = ", y, x , current_value)
        
        # If we reach end of trail and we haven't already been there, add to total
        if grid[y][x] == 9:
            print("trailhead complete!!!")
            trailhead_total += 1
            end_positions.append([[y],[x]])
            visited = [[False] * cols for _ in range(rows)]
            print("backtrack and pop")
            return
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Possible moves
        
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < rows and 0 <= new_x < cols and not visited[new_y][new_x] and grid[new_y][new_x] == current_value + 1:
                print("possible new position = ", new_y, new_x, grid[new_y][new_x])
                visited[new_y][new_x] = True
                
                # Recurse to continue exploring
                dfs(grid, new_y, new_x, visited)

                print("TEST - ", new_y, new_x)
                visited[new_y][new_x] = False

total = 0

for trailhead in trailheads:

    trailhead_total = 0
    end_positions = []

    visited = [[False] * cols for _ in range(rows)]  # 2D array to track visited cells
    visited[0][0] = True  # Mark the start as visited
    dfs(grid, trailhead[0], trailhead[1], visited)
    print(trailhead_total)
    total += trailhead_total


print("Part 1 Answer = ", total)


# Part 2 Plan

