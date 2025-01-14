data_path = './day20_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# Plan
# Dijkstra's Algorithm 
# Then find cheats where there are path squares seperated by a wall

rows, cols = len(data), len(data[0])

# define start and end and create heap for priority queue
import heapq

start = ()
end = ()
heap = [] 

for y, row in enumerate(data):
    for x, column in enumerate(row):
        if row[x] == "S":
            start = (y,x)
            heapq.heappush(heap, (0, (y, x)))
        if row[x] == "E":
            end = (y,x)
        if column == ".":
            heapq.heappush(heap, (float('inf'), (y, x)))

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(data, start):

    # define dictionaries for distances ans predecessors
    dist = {} 
    predecessor = {}

    for y, row in enumerate(data):
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
                if current_dist + 1 < dist[(new_y, new_x)] and data[new_y][new_x] != "#":
                    adjacent_vertices.append([new_y, new_x])
                    add_node(current_dist, (new_y, new_x))
            

    return dist, predecessor
        

distances, predecessors = dijkstra(data, start)

# find shortest path to end
path_data = {key: val for key, val in distances.items() if val != float('inf')}

current_position = end
current_value = int(path_data[(end[0], end[1])])
shortest_path = []
shortest_path.append(current_position)
while current_position != start:
    for dy, dx in directions:
        new_y, new_x = current_position[0] + dy, current_position[1] + dx
        if new_y >= 0 and new_y <= rows and new_x >= 0 and new_x <= cols:
            if data[new_y][new_x] != "#" and int(path_data[(new_y,new_x)]) == current_value - 1:
                current_position = new_y, new_x
                current_value -= 1
                shortest_path.append(current_position)


# print data
data_print = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if (y,x) == start: 
            string += "S"
            continue
        if (y,x) == end: 
            string += "E"
            continue
        if data[y][x] == "#":
            string += "#"
        if data[y][x] == "." and (y,x) in shortest_path: 
            string += "X"
        if data[y][x] == "." and (y,x) not in shortest_path: 
            string += "."

    data_print.append(string)

#print('\n'.join(data_print))

print("Fastest time: ", int(path_data[end]))

print(shortest_path)

# now we want to go through the shortest path and find possible cheats
# we need a function to work out how much time a cheat would save

cheat_locations = []
for location in shortest_path:
    for dy, dx in directions:
        new_y, new_x = location[0] + dy, location[1] + dx
        new2_y, new2_x = location[0] + (2 * dy), location[1] + (2 * dx)
        if new_y >= 0 and new_y <= rows and new_x >= 0 and new_x <= cols and new2_y >= 0 and new2_y <= rows and new2_x >= 0 and new2_x <= cols:
            if data[new_y][new_x] == "#" and (new2_y, new2_x) in shortest_path and (new_y, new_x) not in cheat_locations:
                cheat_locations.append((new_y, new_x))


#print(cheat_locations)


# print data
data_print = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if (y,x) == start: 
            string += "S"
            continue
        if (y,x) == end: 
            string += "E"
            continue
        if (y,x) in cheat_locations:
            string += "@"
            continue
        if data[y][x] == "#":
            string += "#"
        if data[y][x] == "." and (y,x) in shortest_path: 
            string += "X"
        if data[y][x] == "." and (y,x) not in shortest_path: 
            string += "."

    data_print.append(string)

#print('\n'.join(data_print))

def time_saved(cheat_location):
    #print(cheat_location)
    # first find the two path locations either side of the cheat location
    locations = []
    for dy, dx in directions:
        # opposing direcitons
        new_y, new_x = cheat_location[0] + dy, cheat_location[1] + dx
        new2_y, new2_x = cheat_location[0] - dy, cheat_location[1] - dx
        if (new_y, new_x) in shortest_path and (new2_y, new2_x) in shortest_path:
            #print((new_y, new_x), "and", (new2_y, new2_x), " in shortest path")
            locations.append((new_y, new_x))
            locations.append((new2_y, new2_x))
            break

    if len(locations) != 2:
        print("ERROR")
        return -1

    return abs(shortest_path.index(locations[0]) - shortest_path.index(locations[1])) - 2


total = 0

frequencies = {}

for location in cheat_locations:
    saving = time_saved(location)
    if saving in frequencies:
        frequencies[saving] += 1
    else:
        frequencies[saving] = 1

    if time_saved(location) >= 100:
        total += 1


print("Test data frequencies: ", frequencies)
print("Part 1 Solution = ", total)

# Part 2
# for every location in shortest_path, work out which other locations in the path we can get to in less than 20 ps
# work out time saving 


def time_saved2(start, end):
    print(end)
    return shortest_path.index(start) - shortest_path.index(end) - abs(start[0] - end[0]) - abs(start[1] - end[1])

start = shortest_path[-1]
heap = [] 

for y, row in enumerate(data):
    for x, column in enumerate(row):
        if column == "#":
            heapq.heappush(heap, (float('inf'), (y, x)))

heapq.heappush(heap, (0, (3, 1))) # start

def dijkstra2(data, start):

    # define dictionaries for distances ans predecessors
    dist = {} 
    predecessor = {}

    for y, row in enumerate(data):
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
    should_continue = True
    while should_continue:
        if len(pq) == 0:
            print("processed all nodes - no possible path")
            break

        current_dist, current_node = heapq.heappop(pq)

        # If the current distance is greater than the recorded distance, skip it
        if current_dist > dist[current_node]:
            print("current distance is greater than the recorded distance")
            continue
        
        # Explore neighbors
        adjacent_vertices = []
        for dy, dx in directions:
            new_y, new_x = current_node[0] + dy, current_node[1] + dx
            if 0 <= new_y < rows and 0 <= new_x < cols:
                if current_dist + 1 < dist[(new_y, new_x)] and data[new_y][new_x] == "#" and current_dist < 19:
                    adjacent_vertices.append([new_y, new_x])
                    add_node(current_dist, (new_y, new_x))
            

    return dist, predecessor
        

distances, predecessors = dijkstra2(data, start)

# find possible cheats by going through the shortest path and seeing if there are any of the dijkstra locations nearby
location_data = {key: val for key, val in distances.items() if val != float('inf')}

def best_cheat(best, new):
    if best == 0 and new != 0:
        return new
    if best != 0 and new < best:
        return new
    return best

cheat_prints = {}

for location in shortest_path:
    #print("location: ", location)
    best_cheat_val = 0
    for dy, dx in directions:
        new_y, new_x = location[0] + dy, location[1] + dx
        if (new_y, new_x) in location_data:
            #print("possible cheat from: ", new_y, new_x, location_data[(new_y, new_x)])
            best_cheat_val = best_cheat(best_cheat_val, location_data[(new_y, new_x)] + 1)

    if best_cheat_val != 0:
        print("cheat of ", best_cheat_val, "at", location)
        cheat_prints[location] = best_cheat_val



# print data
data_print = []
for y in range(rows):
    string = ""
    for x in range(cols):
        if (y,x) == start: 
            string += "S"
            continue
        if (y,x) in cheat_prints:
            string += str(cheat_prints[(y, x)])[-1]
            continue
        if data[y][x] == "#":
            string += "#"
        if data[y][x] == ".": 
            string += "."

    data_print.append(string)

print('\n'.join(data_print))


#test