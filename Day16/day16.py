import heapq

data_path = './day16_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split('\n')

rows, cols = len(grid), len(grid[0])

# Plan
# Dijkstra's Algorithm 

start = ()
end = ()
heap = [] # this is for priority queue

for y, row in enumerate(grid):
    for x, column in enumerate(row):
        if column == "S":
            start = (y,x)
            heapq.heappush(heap, (0, (y, x)))
        if column == "E":
            end = (y,x)
        if column == ".":
            heapq.heappush(heap, (float('inf'), (y, x)))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

turn = [[False] * cols for _ in range(rows)] 

def dijkstra(grid, start):

    dist = {} # distances
    dirs = {} # directions
    predecessor = {}

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            predecessor[(y, x)] = None
            if column == "S":
                start = (y,x)
                heapq.heappush(heap, (0, (y, x)))
            if column == "E":
                end = (y,x)
            if column == ".":
                heapq.heappush(heap, (float('inf'), (y, x)))
            if column != "S":
                dist[(y, x)] = float('inf')


    dist[start] = 0
    dirs[start] = None
    pq = [(0, start)]

    def add_node(current_distance, new, value):
        if current_distance + value <= dist[(new[0], new[1])]:
            dist[(new[0], new[1])] = current_distance + value
            heapq.heappush(pq, (current_distance + value, (new[0], new[1])))

    current_node = start

    while current_node != end:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            break
        
        # If the current distance is greater than the recorded distance, skip it
        if current_dist > dist[current_node]:
            continue
        
        # Explore neighbors
        adjacent_vertices = []
        for dy, dx in directions:
            new_y, new_x = current_node[0] + dy, current_node[1] + dx
            if 0 <= new_y < rows and 0 <= new_x < cols:
                if current_dist + 1 < dist[(new_y, new_x)] and grid[new_y][new_x] != "#":
                    adjacent_vertices.append([new_y, new_x])

                    # account for the points increase associated with turning
                    dirs[(new_y, new_x)] = (dy, dx)
                    if (current_node[0], current_node[1]) != start:
                        if dirs[(current_node[0], current_node[1])] != dirs[(new_y, new_x)]:
                            turn[current_node[0]][current_node[1]] = True
                            add_node(current_dist, (new_y, new_x), 1001)
                        else:
                            add_node(current_dist, (new_y, new_x), 1)
                    else:
                        if (dy, dx) != (0, 1):
                            add_node(current_dist, (new_y, new_x), 1001)
                        else:
                            add_node(current_dist, (new_y, new_x), 1)
            

    return dist, predecessor
        

distances, predecessors = dijkstra(grid, start)
path_data = {key: val for key, val in distances.items() if val != float('inf')}

# find shortest path to end
current_position = end
current_value = int(path_data[(end[0], end[1])])
shortest_path = set(end)
while current_position != start:
    for dy, dx in directions:
        new_y, new_x = current_position[0] + dy, current_position[1] + dx
        if grid[new_y][new_x] != "#" and (int(path_data[(new_y,new_x)]) == current_value - 1 or int(path_data[(new_y,new_x)]) == current_value - 1001):
            if int(path_data[(new_y,new_x)]) == current_value - 1:
                current_position = new_y, new_x
                current_value -= 1
                shortest_path.add(current_position)
            if int(path_data[(new_y,new_x)]) == current_value - 1001:
                current_position = new_y, new_x
                current_value -= 1001
                shortest_path.add(current_position)


# print grid
grid_print = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if grid[y][x] == "#":
            string += "#"
        if grid[y][x] == "." and (y,x) in shortest_path: 
            string += "X"
        if grid[y][x] == "." and (y,x) not in shortest_path: 
            string += "."
        if (y,x) == start: 
            string += "S"
        if (y,x) == end: 
            string += "E"

    grid_print.append(string)

print('\n'.join(grid_print))

print("Part 1 Solution: ", int(path_data[end]))

shortest_paths = set()

def dfs(grid, y, x, visited):
        global spots
        current_value = int(path_data[(y,x)])
        
        if (y, x) == start:            
            shortest_paths.add((y, x))
        
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if (new_y, new_x) in path_data:
                if 0 <= new_y < rows and 0 <= new_x < cols and grid[new_y][new_x] != "#" and not visited[new_y][new_x] and (int(path_data[(new_y,new_x)]) == current_value - 1 or int(path_data[(new_y,new_x)]) == current_value - 1001 or (int(path_data[(new_y,new_x)]) == current_value + 999) and turn[y][x] == True):
                    shortest_paths.add((new_y,new_x))
                    visited[new_y][new_x] = True
                    dfs(grid, new_y, new_x, visited) # Recurse to continue exploring
                    visited[new_y][new_x] = False



visited = [[False] * cols for _ in range(rows)] 
visited[0][0] = True  
dfs(grid, end[0], end[1], visited)

shortest_paths.add(end)


grid_print2 = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if grid[y][x] == "#":
            string += "#"
        if (y,x) in shortest_paths: 
            string += "X"
        if grid[y][x] == "." and (y,x) not in shortest_paths: 
            string += "."

    grid_print2.append(string)

print('\n'.join(grid_print2))

print("Part 2 Solution: ", len(shortest_paths))