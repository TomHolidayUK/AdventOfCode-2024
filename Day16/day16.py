import heapq

data_path = './day16_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split('\n')

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

sptSet = set()
position = start 
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while position != end:
    # find smallest value in priority queue / heap
    smallest_value, smallest_coordinate = heapq.heappop(heap)
    print(f"Smallest value is {smallest_value} at coordinate {smallest_coordinate}")

    # find adjacent vertices
    adjacent_vertices = []
    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx
        if grid[new_y][new_x] != "#":
            adjacent_vertices.append([new_y, new_x])
    
    for vertex in adjacent_vertices:
        






