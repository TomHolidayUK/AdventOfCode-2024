data_path = './day12_data_test.txt'

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
in_group = set()

def find_group(y, x, visited):
        
        #print("current pos: ", x, y)

        # avoid repetition
        if (y,x) in in_group:
            return

        groups[grid[y][x]].add((y,x))
        in_group.add((y,x))
              
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx

            if 0 <= new_y < rows and 0 <= new_x < cols and not visited[new_y][new_x] and grid[new_y][new_x] == grid[y][x]:
                visited[new_y][new_x] = True
                
                # Recurse to continue exploring
                find_group(new_y, new_x, visited)

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

def perimeter_trace(group_identifier, edges, start_y, start_x, start_direction):
    # this traces a perimeter of a group counting the number of turns and addig to the edges list

    trace = set()

    current_y, current_x =  start_y, start_x
    current_direction = start_direction

    while((current_y, current_x) not in trace and current_direction not in trace):
        print("current position: ", current_y, current_x)
        print("current direction: ", current_direction)

        # add current pedge to edges
        edges.append([current_y, current_x, current_direction])

        # calculate next position and direction
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W

        # check if we need to turn
        dy, dx = directions[current_direction][0], directions[current_direction][1]
        next_y, next_x = plot[0] + dy, plot[1] + dx
        if (next_y, next_x) in groups[group_identifier]:
            print("no need to turn")
            current_y, current_x = next_y, next_x
            continue

        # turn until current square in in same group
        while ((current_y, current_x) not in groups[group_identifier]):
            print("turning")
            current_direction = (i + 1) % 4
            dy, dx = directions[current_direction][0], directions[current_direction][1]
            current_y, current_x = plot[0] + dy, plot[1] + dx


    # is there a plot that is part of the same group there or do we need to turn
    dy, dx = directions[current_direction][0], directions[current_direction][1]
    current_y, current_x = plot[0] + dy, plot[1] + dx
    print("current: ", current_y, current_x)


def sides(group_identifier):

    sides_total = 0

    # # find the top left most square, find it's top edge
    # group = list(groups[group_identifier])  
    # miny = group[0][0]  
    # minx = group[0][1]  

    # for plot in group:
    #     if plot[0] < miny:
    #         miny = plot[0]
    #     if plot[1] < minx:
    #         minx = plot[1]

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # N, E, S, W

    edges = []

    perimeter_trace(group_identifier, edges, 0, 1, 1)

    # for plot in groups[group_identifier]:
    #     print(plot)
    #     for i, direction in enumerate(directions):
    #         dy, dx = direction
    #         new_y, new_x = plot[0] + dy, plot[1] + dx
    #         if (new_y, new_x) not in groups[group_identifier]:
    #             print("found edge: ", new_y, new_x)
    #             # found edge, now trace this perimeter all the way and count the number of changes in direction
    #             trace_direction = (i + 1) % 4
    #             perimeter_trace(group_identifier, edges, plot[0], plot[1], trace_direction)







    # # trace the edge of the perimeter, recording each time we change direction
    # current_location = [miny, minx]
    # print(current_location)
    # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # N, E, S, W
    # current_direction = 0
    # dy, dx = directions[current_direction][0], directions[current_direction][1]
    # new_y, new_x = y + dy, x + dx

    # if (new_y, new_x) not in groups[group_identifier]:
    #     print("need to change direction")
    #     current_direction += 1
    #     if current_direction == 4:
    #         current_direction = 0
        





    # go all the way to we reach the start position's top edge again

total = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (y,x) not in in_group:
            print("searching for ", y, x)
            value = grid[y][x]
            groups[value] = set()
            find_group(y, x, visited)
            #print(groups)
            total += len(groups[value]) * perimeter(value)
            #print(total)

print("Part 1 Total = ", total)

value = grid[0][0]
# find_grid(0, 0, visited)
# print(groups)
# print(perimeter(value))
print(sides(value))

