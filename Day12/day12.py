data_path = './day12_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split()


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
groups_list = []
in_group = set()

def find_group(y, x, visited, group_number):
        
        #print("current pos: ", x, y)

        # avoid repetition
        if (y,x) in in_group:
            return

        groups[grid[y][x]].add((y,x))
        groups_list[group_number][1].append([y, x])
        in_group.add((y,x))
              
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < rows and 0 <= new_x < cols and not visited[new_y][new_x] and grid[new_y][new_x] == grid[y][x]:
                visited[new_y][new_x] = True
                
                # Recurse to continue exploring
                find_group(new_y, new_x, visited, group_number)

                # after exploring all possible paths from current cell mark as not visited so it can be included in other paths
                # this essentially allows backtracking
                visited[new_y][new_x] = False


visited = [[False] * cols for _ in range(rows)]  
visited[0][0] = True
value = grid[0][0]

def perimeter(group_identifier):
    perimeter = 0 
    for plot in groups[group_identifier]:
        y, x = plot[0], plot[1]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if (new_y, new_x) not in groups[group_identifier]:
                perimeter += 1
    return perimeter

def perimeter_trace(group_number, edges, start_y, start_x, start_direction):
    # this traces a perimeter of a group counting the number of turns and addig to the edges list
    
    trace = set()
    turns = 0

    current_y, current_x =  start_y, start_x
    current_direction = start_direction

    while((current_y, current_x, current_direction) not in trace):
        # add current edge to edges
        edges.append([current_y, current_x, current_direction])
        trace.add((current_y, current_x, current_direction))

        # calculate next position and direction
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W

        # always try to turn left if possible
        next_direction = (current_direction - 1) % 4
        dy, dx = directions[next_direction][0], directions[next_direction][1]
        next_y, next_x = current_y + dy, current_x + dx
        if [next_y, next_x] in groups_list[group_number][1]:
            turns += 1
            current_y, current_x = next_y, next_x
            current_direction = next_direction
            continue

        # check if we need to turn
        dy, dx = directions[current_direction][0], directions[current_direction][1]
        next_y, next_x = current_y + dy, current_x + dx
        if [next_y, next_x] in groups_list[group_number][1]:
            current_y, current_x = next_y, next_x
            continue

        # turn until current square in in same group
        turning = True
        start_direction = current_direction

        while (turning == True):
            current_direction = (current_direction + 1) % 4

            if current_direction == start_direction:
                # we have fully turned around, this must be a plot of area 1"

                turns += 1
                turning = False
                continue

            dy, dx = directions[current_direction][0], directions[current_direction][1]
            next_y, next_x = current_y + dy, current_x + dx

            if (current_y, current_x, current_direction) in trace:
                # back at start, end
                turns += 1
                break

            turns += 1

            edges.append([current_y, current_x, current_direction])
            trace.add((current_y, current_x, current_direction))
            if [next_y, next_x] in groups_list[group_number][1]:
                # found a path 
                current_y, current_x = next_y, next_x
                turning = False
            
    return turns


def sides(group_no):

    sides_total = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W

    edges = []

    for plot in groups_list[group_no][1]:
        for i, direction in enumerate(directions):
            # we check for non group plots to the left of the direction of travel
            check_direction = (i - 1) % 4
            dy, dx = directions[check_direction][0], directions[check_direction][1]
            new_y, new_x = plot[0] + dy, plot[1] + dx
            if [new_y, new_x] not in groups_list[group_no][1]:
                # found edge, now trace this perimeter all the way and count the number of changes in direction
                if ([plot[0], plot[1], i] not in edges):
                    sides_total += perimeter_trace(group_no, edges, plot[0], plot[1], i)
    
    return sides_total


total = 0
group_no = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (y,x) not in in_group:
            value = grid[y][x]
            groups[value] = set()
            groups_list.append([value, []])
            find_group(y, x, visited, group_no)
            total += len(groups[value]) * perimeter(value)
            group_no += 1
print("Part 1 Total = ", total)

total2 = 0

for group_no, group in enumerate(groups_list):
    group_identifier, data = group[0], group[1]
    number_of_sides = sides(group_no)
    total2 += len(data) * number_of_sides


print("Part 2 Total = ", total2)

