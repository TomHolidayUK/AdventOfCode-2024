data_path = './day6_data_test.txt'

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
        
print("start location is: ", start_location[0], start_location[1])

print("grid is ", height, " by ", width)

# coordinate system = (x,y)

visited_squares = set() # set used because it will only accept unique value (we don';'t want duplicates)

def coordinate_to_index(x,y):
    return (y  * (width + 1)) + x 

def calculate_next_location(current_location, current_direction):
    if current_direction == "U":
        return [current_location[0], current_location[1] - 1]
    # FINISH THIS

def next_location_value(next_location):
    # FINISH THIS
    print("FINSIH")

at_edge = False
current_direction = "U" # up
current_location = start_location

print(calculate_next_location(current_location,current_direction))

while (at_edge == False):

    # calculate next position based on current direction and location

    # if next position is a '#', then change direction clockwise


    # if we reach the edge, we have finished so exit the loop
    if (x == 0) or (y == 0) or (x == width - 1) or (y == height - 1):
        et_edge = True

    
