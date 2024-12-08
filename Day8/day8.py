data_path = './day8_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split('\n')

# Plan
# 1 - create matrix of antennae locations for different frequencies
# 2 - for each anntenae frequency, create unique pairs of antennae (use itertools)
# 3 - for each unique pair work out antinode locations using trigonometry
# 4 - add locations to a set so they can't be repeated, find total size of set

# Part 1
antenna_locations = dict()

height = 0 
width = 0 

for y, line in enumerate(grid):
    height += 1
    for char in line:
        if (y == 0):
            width += 1

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if (char != ".") and (char != "#"):
            if char not in antenna_locations:
                antenna_locations[char] = [[x,y]]
            else:
                existing_value = antenna_locations[char]
                existing_value.append([x,y])
                antenna_locations[char] = existing_value

antinodes_part_1 = set()
antinodes_part_2 = set()

# Part 2
def find_unique_pairs(size):
    unique_pairs = []
    for i in range(size):
        for j in range(size):
            if ([j,i] not in unique_pairs) and (i != j):
                unique_pairs.append([i,j])

    return unique_pairs

def in_grid(location):
    if location[0] < 0 or location[0] > width - 1 or location[1] < 0 or location[1] > height - 1:
        return False
    else:
        return True
    
def coordinate_to_index(location):
    x = location[0]
    y = location[1]
    return (y  * (width + 1)) + x 


for key, value in antenna_locations.items():
    unique_pairs = find_unique_pairs(len(value))

    # Part 3
    for pair in unique_pairs:
        location_1 = value[pair[0]]
        location_2 = value[pair[1]]

        antinode_1_x = (2 * location_1[0]) - location_2[0]
        antinode_1_y = (2 * location_1[1]) - location_2[1]
        antinode_2_x = (2 * location_2[0]) - location_1[0]
        antinode_2_y = (2 * location_2[1]) - location_1[1] 

        antinode_1 = [antinode_1_x, antinode_1_y]
        antinode_2 = [antinode_2_x, antinode_2_y]

        # Check if within the grid
        if in_grid(antinode_1):
            antinodes_part_1.add(coordinate_to_index(antinode_1))
        if in_grid(antinode_2):
            antinodes_part_1.add(coordinate_to_index(antinode_2))

        # For part 2 antinodes we need to first work out the angle of a pair

        # angle = [change in x, change in y]
        angle = [(location_2[0] - location_1[0]), (location_2[1] - location_1[1])]

        # move at that angle in both directions until reaching edge of grid
        current_location = location_1
        while in_grid(current_location):
            antinodes_part_2.add(coordinate_to_index(current_location))
            current_location = [current_location[0] + angle[0], current_location[1] + angle[1]]

        current_location = location_1
        while in_grid(current_location):
            antinodes_part_2.add(coordinate_to_index(current_location))
            current_location = [current_location[0] - angle[0], current_location[1] - angle[1]]


print("Part 1 Solution = ", len(antinodes_part_1))
print("Part 2 Solution = ", len(antinodes_part_2))



    