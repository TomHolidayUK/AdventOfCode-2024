data_path = './day4_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

#PLAN
# 1 - traverse through the grid looking for potential starts of the pattern 'XMAS' so the char 'X'.
#     will need to establish a coordinate system to do this
# 2 - at each X, work out in which directions there could possibly be a match. (If next to the right 
#     border there shouldn't be a pattern going right)
# 3 - record number and coordinates of all patterns

# 1 - traverse through grid
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

def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

def check(x, y, direction):
    index = coordinate_to_index(x,y)
    if file_content[index] == direction:
        return True
    else:
        return False

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'X':
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
                if check(x,y-1,'M') and check(x,y-2,'A') and check(x,y-3,'S'):
                    total += 1
            if valid_directions['NE'] == True:
                if check(x+1,y-1,'M') and check(x+2,y-2,'A') and check(x+3,y-3,'S'):
                    total += 1
            if valid_directions['E'] == True:
                if check(x+1,y,'M') and check(x+2,y,'A') and check(x+3,y,'S'):
                    total += 1
            if valid_directions['SE'] == True:
                if check(x+1,y+1,'M') and check(x+2,y+2,'A') and check(x+3,y+3,'S'):
                    total += 1
            if valid_directions['S'] == True:
                if check(x,y+1,'M') and check(x,y+2,'A') and check(x,y+3,'S'):
                    total += 1
            if valid_directions['SW'] == True:
                if check(x-1,y+1,'M') and check(x-2,y+2,'A') and check(x-3,y+3,'S'):
                    total += 1
            if valid_directions['W'] == True:
                if check(x-1,y,'M') and check(x-2,y,'A') and check(x-3,y,'S'):
                    total += 1
            if valid_directions['NW'] == True:
                if check(x-1,y-1,'M') and check(x-2,y-2,'A') and check(x-3,y-3,'S'):
                    total += 1


print("Part 1 Total = ", total)

total2 = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == 'A':
            # check start is valid
            if (y > 0) and (x < width - 1) and (y < height - 1) and (x > 0):
                # 3 - check if there are any matches
                if check(x-1,y-1,'M') and check(x+1,y-1,'S') and check(x+1,y+1,'S') and check(x-1,y+1,'M'):
                    total2 += 1
                if check(x-1,y-1,'M') and check(x+1,y-1,'M') and check(x+1,y+1,'S') and check(x-1,y+1,'S'):
                    total2 += 1
                if check(x-1,y-1,'S') and check(x+1,y-1,'S') and check(x+1,y+1,'M') and check(x-1,y+1,'M'):
                    total2 += 1
                if check(x-1,y-1,'S') and check(x+1,y-1,'M') and check(x+1,y+1,'M') and check(x-1,y+1,'S'):
                    total2 += 1
            

print("Part 2 Total = ", total2)



