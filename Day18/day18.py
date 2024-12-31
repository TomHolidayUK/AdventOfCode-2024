data_path = './day18_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# Plan - Dijkstra's Algorithm (re-use code from Day 16)

SIZE = 6
#SIZE = 70

BYTE_LIMIT = 12
# BYTE_LIMIT = 1024

rows, cols = SIZE + 1, SIZE + 1

grid = []

for y in range(rows):
    row = ""
    for x in range(cols):
        row += "."
    grid.append(row)

for i in range(BYTE_LIMIT):
    byte = data[i]
    x_string, y_string = byte.split(",")
    x, y = int(x_string), int(y_string)
    grid[y] = grid[y][:x] + "#" + grid[y][x+1:]

# define start and end and create heap for priority queue
import heapq

start = ()
end = ()
heap = [] 

for y, row in enumerate(grid):
    for x, column in enumerate(row):
        if y == 0 and x == 0:
            start = (y,x)
            heapq.heappush(heap, (0, (y, x)))
        if y == SIZE and x == SIZE:
            end = (y,x)
        if column == ".":
            heapq.heappush(heap, (float('inf'), (y, x)))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(grid, start):

    # define dictionaries for distances ans predecessors
    dist = {} 
    predecessor = {}

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            predecessor[(y, x)] = None
            if (y,x) != start:
                dist[(y, x)] = float('inf')


    dist[start] = 0
    pq = [(0, start)]

    # add node if there is a shorter distances to that node than currently exists 
    def add_node(current_distance, new):
        if current_distance + 1 <= dist[(new[0], new[1])]:
            dist[(new[0], new[1])] = current_distance + 1
            heapq.heappush(pq, (current_distance + 1, (new[0], new[1])))

    current_node = start

    # loop until at the end or until no more possible paths
    while current_node != end:
        if len(pq) == 0:
            print("processed all nodes - no possible path")
            break

        current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            print("AT END")
            break
        
        # If the current distance is greater than the recorded distance, skip it
        if current_dist > dist[current_node]:
            print("current distance is greater than the recorded distance")
            continue
        
        # Explore neighbors
        adjacent_vertices = []
        for dy, dx in directions:
            new_y, new_x = current_node[0] + dy, current_node[1] + dx
            if 0 <= new_y < rows and 0 <= new_x < cols:
                if current_dist + 1 < dist[(new_y, new_x)] and grid[new_y][new_x] != "#":
                    adjacent_vertices.append([new_y, new_x])
                    add_node(current_dist, (new_y, new_x))
            

    return dist, predecessor
        

distances, predecessors = dijkstra(grid, start)

# find shortest path to end
path_data = {key: val for key, val in distances.items() if val != float('inf')}

current_position = end
current_value = int(path_data[(end[0], end[1])])
shortest_path = set(end)
while current_position != start:
    for dy, dx in directions:
        new_y, new_x = current_position[0] + dy, current_position[1] + dx
        if new_y >= 0 and new_y <= SIZE and new_x >= 0 and new_x <= SIZE:
            if grid[new_y][new_x] != "#" and int(path_data[(new_y,new_x)]) == current_value - 1:
                current_position = new_y, new_x
                current_value -= 1
                shortest_path.add(current_position)


# print grid
grid_print = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if (y,x) == start: 
            string += "S"
            continue
        if (y,x) == end: 
            string += "E"
            continue
        if grid[y][x] == "#":
            string += "#"
        if grid[y][x] == "." and (y,x) in shortest_path: 
            string += "X"
        if grid[y][x] == "." and (y,x) not in shortest_path: 
            string += "."

    grid_print.append(string)

print('\n'.join(grid_print))

print("Part 1 Solution: ", int(path_data[end]))#

# Part 2

possible = True
BYTE_LIMIT = 0

while possible == True:

    print("BYTE LIMIT = ", BYTE_LIMIT, data[BYTE_LIMIT - 1])

    grid = []

    for y in range(rows):
        row = ""
        for x in range(cols):
            row += "."
        grid.append(row)

    for i in range(BYTE_LIMIT):
        byte = data[i]
        x_string, y_string = byte.split(",")
        x, y = int(x_string), int(y_string)
        grid[y] = grid[y][:x] + "#" + grid[y][x+1:]

    print(grid)

    # define start and end and create heap for priority queue
    import heapq

    start = ()
    end = ()
    heap = [] 

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if y == 0 and x == 0:
                start = (y,x)
                heapq.heappush(heap, (0, (y, x)))
            if y == SIZE and x == SIZE:
                end = (y,x)
            if column == ".":
                heapq.heappush(heap, (float('inf'), (y, x)))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dijkstra(grid, start):

        global possible

        # define dictionaries for distances ans predecessors
        dist = {} 
        predecessor = {}

        for y, row in enumerate(grid):
            for x, column in enumerate(row):
                predecessor[(y, x)] = None
                if (y,x) != start:
                    dist[(y, x)] = float('inf')


        dist[start] = 0
        pq = [(0, start)]

        # add node if there is a shorter distances to that node than currently exists 
        def add_node(current_distance, new):
            if current_distance + 1 <= dist[(new[0], new[1])]:
                dist[(new[0], new[1])] = current_distance + 1
                heapq.heappush(pq, (current_distance + 1, (new[0], new[1])))

        current_node = start

        # loop until at the end or until no more possible paths
        while current_node != end:
            if len(pq) == 0:
                print("processed all nodes - no possible path")
                possible = False
                break

            current_dist, current_node = heapq.heappop(pq)
            if current_node == end:
                print("AT END")
                possible = True
                break
            
            # If the current distance is greater than the recorded distance, skip it
            if current_dist > dist[current_node]:
                print("current distance is greater than the recorded distance")
                continue
            
            # Explore neighbors
            adjacent_vertices = []
            for dy, dx in directions:
                new_y, new_x = current_node[0] + dy, current_node[1] + dx
                if 0 <= new_y < rows and 0 <= new_x < cols:
                    if current_dist + 1 < dist[(new_y, new_x)] and grid[new_y][new_x] != "#":
                        adjacent_vertices.append([new_y, new_x])
                        add_node(current_dist, (new_y, new_x))
                

        return dist, predecessor
            

    distances, predecessors = dijkstra(grid, start)

    if possible:
        # find shortest path to end
        path_data = {key: val for key, val in distances.items() if val != float('inf')}

        current_position = end
        current_value = int(path_data[(end[0], end[1])])
        shortest_path = set(end)
        while current_position != start:
            for dy, dx in directions:
                new_y, new_x = current_position[0] + dy, current_position[1] + dx
                if new_y >= 0 and new_y <= SIZE and new_x >= 0 and new_x <= SIZE:
                    if grid[new_y][new_x] != "#" and int(path_data[(new_y,new_x)]) == current_value - 1:
                        current_position = new_y, new_x
                        current_value -= 1
                        shortest_path.add(current_position)


        # print grid
        grid_print = []
        for y in range(rows):
            string = ""
            for x in range(cols):
                if (y,x) == start: 
                    string += "S"
                    continue
                if (y,x) == end: 
                    string += "E"
                    continue
                if grid[y][x] == "#":
                    string += "#"
                if grid[y][x] == "." and (y,x) in shortest_path: 
                    string += "X"
                if grid[y][x] == "." and (y,x) not in shortest_path: 
                    string += "."

            grid_print.append(string)

        print('\n'.join(grid_print))

        BYTE_LIMIT += 1

    else:
        print("Not possible because of ", data[BYTE_LIMIT - 1])

