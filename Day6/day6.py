data_path = './day6_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


# Plan
# 1 - create coordinate system for the data
# 2 - find starting position
# 3 - create an iterative process where :
#     the guard travels and records the NEW squares it crosses
#     turns right before hitting a #
#     if about to leave the grid, stop the loop and return the total number of squares visited (including starting position)


grid = file_content.split('\n')

height = 0 
width = 0

start_location = []

for y, line in enumerate(grid):
    height += 1
    for x, char in enumerate(line):
        if y == 0:
            width += 1
        if char == '^':
            start_location = [x,y]
        
print("Start location is: (", start_location[0], ",", start_location[1], ")")
print("Grid is ", height, "x", width)

# coordinate system = (x,y)

def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

def calculate_next_location(current_location, current_direction):
    if current_direction == "N":
        return [current_location[0], current_location[1] - 1]
    if current_direction == "E":
        return [current_location[0] + 1, current_location[1]]
    if current_direction == "S":
        return [current_location[0], current_location[1] + 1]
    if current_direction == "W":
        return [current_location[0] - 1, current_location[1]]
    

def next_location_value(next_location):
    next_index = coordinate_to_index(next_location[0], next_location[1])
    return file_content[next_index]

at_edge = False
current_direction = "N" # north
current_location = start_location
changed_direction = False
visited_squares = set() # set used because it will only accept unique value (we don';'t want duplicates)

while not at_edge:

    # print("current location = ", current_location)
    # print("current direction = ", current_direction)

    # add current location to set, the set won't allow duplicates
    visited_squares.add(coordinate_to_index(current_location[0], current_location[1]))

    # calculate next position based on current direction and location
    next_location = calculate_next_location(current_location, current_direction)

    # if next position is a '#', then change direction clockwise
    if next_location_value(next_location) == "#":
        if current_direction == "N":
            current_direction = "E"
        elif current_direction == "E":
            current_direction = "S"
        elif current_direction == "S":
            current_direction = "W"
        elif current_direction == "W":
            current_direction = "N"

        # if we hit a # we need to re-calculate a different next location
        next_location = calculate_next_location(current_location, current_direction)

    # if we reach the edge, we have finished so exit the loop
    if (next_location[0] == 0) or (next_location[1] == 0) or (next_location[0] == width - 1) or (int(next_location[1]) == int(height - 1)):
        print("Reached the edge at ", next_location)
        visited_squares.add(coordinate_to_index(next_location[0], next_location[1]))
        at_edge = True
    else:
        current_location = next_location

    
print("Part 1 Solution = ", len(visited_squares))

# Part 2 Plan 
# 1 - go through all squares on the grid that aren't already a # or ^
# 2 - test if we go into an infinite loop here 
#     (we can test if we go into an infinte loop by seeing if we end up in a position and direction that we've had before)

part2_total = 0 

for x in range(len(file_content)):
    # loop through all "." and create a new grid to test with 
    file_content_copy = file_content
    if file_content[x] == ".":
        file_content_copy = file_content_copy[:x] + "#" + file_content_copy[x + 1:]

    # print(file_content_copy)

    grid = file_content_copy.split('\n')

    def next_location_value_part2(next_location):
        next_index = coordinate_to_index(next_location[0], next_location[1])
        return file_content_copy[next_index]

    # now with our copy ready, see if it goes into an infinite loop
    # we need to record all previous locations and directions
    # each element will be of form [index, direction]
    location_and_direction_record = []

    current_location = start_location
    should_continue = True
    current_direction = "N"

    while should_continue:

        # print("current location = ", current_location)
        # print("current direction = ", current_direction)

        # add current location and direction to record
        location_and_direction_record.append([coordinate_to_index(current_location[0], current_location[1]), current_direction])

        # calculate next position based on current direction and location
        next_location = calculate_next_location(current_location, current_direction)

        # if next position is a '#', then change direction clockwise
        if next_location_value_part2(next_location) == "#":
            if current_direction == "N":
                current_direction = "E"
            elif current_direction == "E":
                current_direction = "S"
            elif current_direction == "S":
                current_direction = "W"
            elif current_direction == "W":
                current_direction = "N"

            # if we hit a # we need to re-calculate a different next location
            next_location = calculate_next_location(current_location, current_direction)

        # if we reach the edge, we have finished so exit the loop
        if (next_location[0] == 0) or (next_location[1] == 0) or (next_location[0] == width - 1) or (int(next_location[1]) == int(height - 1)):
            #print("Reached the edge at ", next_location)
            should_continue = False
        # if we have been in the current position with the same directions before
        elif [coordinate_to_index(next_location[0], next_location[1]), current_direction] in location_and_direction_record:
            part2_total += 1
            should_continue = False
        else:    
            current_location = next_location


print("Part 2 Solution = ", part2_total)
