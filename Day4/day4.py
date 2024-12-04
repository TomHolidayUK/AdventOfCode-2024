data_path = './day4_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

#PLAN
# 1 - traverse through the grid looking for potential starts of the pattern 'XMAS' so the char 'X'.
#     will need to establish a coordinate system to do this
# 2 - at each X, work out in which directions there could possibly be a match. (If next to the right 
#     border there souldn't be a pattern going right)
# 3 - record number and coordinates of all patterns

# 1

grid = file_content.split('\n')

height = 0 
width = 0

for y, line in enumerate(grid):
    height += 1
    if y is 0:
        for x, char in enumerate(line):
            width += 1

print("grid is ", height, " by ", width)

# coordinate system = (x,y)

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

def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char is 'X':
            print(char, x, y, file_content[coordinate_to_index(x,y)])
            # 2 - we will first assume all directions are valid but rule certain ones out
            # if too close to top
            # if too close to right
            # if too close to bottom 
            # if too close to left

