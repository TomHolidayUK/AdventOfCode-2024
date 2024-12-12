data_path = './day12_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split()

print(grid)

# Plan
# Write a function that finds the total area for a square
# It will recursively search for all conjoined squares and record their position
# I think we use DFS again because it is best at finding all possible paths
# We need to record all the squares that have already been assigned to a group so that we don't 
# calculate it's group again
# Once we have all the group coordinates we can work out their area and perimeter

rows, cols = len(grid), len(grid[0])

# create dictionary to contain sets of the different groups
groups = {}
in_group = set()

def find_grid(y, x, visited):
        
        #print("current pos: ", x, y)

        groups[grid[y][x]].add((y,x))
        in_group.add((y,x))
              
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Possible moves
        
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < rows and 0 <= new_x < cols and not visited[new_y][new_x] and grid[new_y][new_x] == grid[y][x]:
                visited[new_y][new_x] = True
                
                # Recurse to continue exploring
                find_grid(new_y, new_x, visited)

                # after exploring all possible paths from current cell mark as not visited so it can be included in other paths
                # this essentially allows backtracking
                visited[new_y][new_x] = False


visited = [[False] * cols for _ in range(rows)]  # 2D array to track visited cells
visited[0][0] = True
value = grid[0][0]

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (y,x) not in in_group:
            print("searching for ", y, x)
            value = grid[y][x]
            groups[value] = set()
            find_grid(y, x, visited)
            print(groups)
