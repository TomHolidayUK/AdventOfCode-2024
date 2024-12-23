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


def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(grid, start):

    sptSet = set()

    dist = {}
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


    smallest_value, smallest_coordinate = heapq.heappop(heap)
    print(f"Smallest initial value (the start) is {smallest_value} at coordinate {smallest_coordinate}")

    dist[start] = 0
    print("dist: ", dist)
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node not in sptSet:
            sptSet.add(current_node)
            print("current node = ", current_node, "dist: ", current_dist)
            
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
                        print("adding ", new_y, new_x, " to adjacent vertices")
                        adjacent_vertices.append([new_y, new_x])
                        heapq.heappush(pq, (current_dist + 1, (new_y, new_x)))
                        dist[(new_y, new_x)] = current_dist + 1
            
            for vertex in adjacent_vertices:
                distance = current_dist + 1
                if distance < dist[(new_y, new_x)] and grid[new_y][new_x] != "#":
                    print("shorter path to neighbour found for ", new_y, new_x)
                    dist[(new_y, new_x)] = distance
                    predecessor[(new_y, new_x)] = current_node
                    heapq.heappush(pq, (distance, (new_y, new_x)))
        else:
            print("already visited this square")


    return dist, predecessor
        

distances, predecessors = dijkstra(grid, start)
filtered_data = {key: val for key, val in distances.items() if val != float('inf')}
#print(f"Shortest distances from node {start}: {filtered_data}")

grid_print = []

for y in range(rows):
    string = ""
    for x in range(cols):
        if grid[y][x] == "#":
            string += "#"
        else: 
            length = len(str(filtered_data[(y, x)]))
            string += str(filtered_data[(y, x)])[length - 1]

    grid_print.append(string)

print('\n'.join(grid_print))

# find shortest path to end
current_position = end
current_value = int(filtered_data[(end[0], end[1])])
shortest_path = [end]
while current_position != start:
    print(current_position, current_value)
    for dy, dx in directions:
        new_y, new_x = current_position[0] + dy, current_position[1] + dx
        if grid[new_y][new_x] != "#" and int(filtered_data[(new_y,new_x)]) == current_value - 1:
            print(new_y, new_x, " is ", int(filtered_data[(new_y,new_x)]))
            if int(filtered_data[(new_y,new_x)]) == current_value - 1:
                current_position = new_y, new_x
                current_value -= 1
                shortest_path.append(current_position)

print(shortest_path)

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

    grid_print.append(string)



print('\n'.join(grid_print))



