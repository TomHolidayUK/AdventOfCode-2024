data_path = './day4_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

#PLAN
# 1 - traverse through the grid looking for potential starts of the pattern 'XMAS' so the char 'X'.
#     will need to establish a coordinate system to do this
# 2 - at each X, work out in which directions there could possibly be a match. (If next to the right 
#     border there shouldn't be a pattern going right)
# 3 - record number and coordinates of all patterns

# 1

grid = file_content.split('\n')

height = 0 
width = 0

for y, line in enumerate(grid):
    height += 1
    if y == 0:
        for x, char in enumerate(line):
            width += 1

print("grid is ", height, " by ", width)

# coordinate system = (x,y)

total = 0

def check(int, direction):
    if file_content[int] == direction:
        return True
    else:
        return False

def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'X':
            #print(char, x, y, file_content[coordinate_to_index(x,y)])

            # 2 - we will first assume all directions are valid but rule certain ones out
            valid_directions = {
                "N": True,
                "NE": True,
                "E": True,
                "SE": True,
                "S": True,
                "SW": True,
                "W": True,
                "NW": True,
            }
            # if too close to top
            if (y < 3):
                valid_directions['N'] = False
                valid_directions['NE'] = False
                valid_directions['NW'] = False
            # if too close to right
            if (x > width - 4):
                valid_directions['E'] = False
                valid_directions['NE'] = False
                valid_directions['SE'] = False
            # if too close to bottom 
            if (y > height - 4):
                valid_directions['S'] = False
                valid_directions['SE'] = False
                valid_directions['SW'] = False
            # if too close to left
            if (x < 3):
                valid_directions['W'] = False
                valid_directions['NW'] = False
                valid_directions['SW'] = False

            # 3 - check if there are any matches

            if valid_directions['N'] == True:
                print(x,y)
                #6,4
                if file_content[coordinate_to_index(x,y-1)] == 'M' and file_content[coordinate_to_index(x,y-2)] == 'A' and file_content[coordinate_to_index(x,y-3)] == 'S':
                    print("N match found for ", x,y)
                    total += 1





