import re

data_path = './day14_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Plan
# Record starting position of all robots
# Write a move function that calculates a robots new coordinates after moving (including when they teleport)
# Apply move function to each robot 100 times
# Work out which robot is in which quadrant

rows = file_content.split('\n')
# height = 7
height = 103
# width = 11
width = 101

# Record starting position of all robots
robots = []
for row in rows:
    robot = []
    parts = row.split(",")
    robot.append(int(parts[0].split("=")[1]))
    robot.append(int(parts[1].split(" ")[0]))
    robot.append(int(parts[1].split("=")[1]))
    robot.append(int(parts[2]))
    robots.append(robot)


# Write a move function that calculates a robots new coordinates after moving (including when they teleport)
def move(start_x, start_y, vel_x, vel_y):
    new_x, new_y = start_x + vel_x, start_y + vel_y
    if new_x < 0:
        new_x += width
    if new_y < 0:
        new_y += height
    if new_x > width - 1:
        new_x -= width
    if new_y > height - 1:
        new_y -= height

    return new_x, new_y


final_positions = []

# Apply move function to each robot 100 times
for robot in robots:
    x, y = robot[0], robot[1]
    for i in range(100):
        x, y = move(x, y, robot[2], robot[3])
    final_positions.append([x, y])

print(len(final_positions))

# Work out which robot is in which quadrant
q1, q2, q3, q4 = 0, 0, 0, 0
left_robots, right_robots = [], []
for position in final_positions:
    x, y = position[0], position[1]
    if x < int((width / 2) - 0.5) and y < int(height / 2 - 0.5):
        q1 += 1
        left_robots.append([x,y])
    if x >= int(width / 2 + 0.5) and y < int(height / 2 - 0.5):
        q2 += 1
        right_robots.append([x,y])
    if x >= int(width / 2 + 0.5) and y >= int(height / 2 + 0.5):
        q3 += 1
        right_robots.append([x,y])
    if x < int(width / 2 - 0.5) and y >= int(height / 2 + 0.5):
        q4 += 1
        left_robots.append([x,y])


print("Part 1 Total = ", q1 * q2 * q3 * q4)

# Part 2 Plan
# Look for patterns in the robots??? 
# Try to find symmetry in the robots shape??? 
# Or try to find them all next to each other???
# We need to be able to print the robots shape to visualise them

def print_positions(positions):
    data_path = './day14_data.txt'
    with open("./positions.txt", "w") as file:
        # loop through all possible positions and see if there are robots there
        for y in range(height):
            for x in range(width):
                num = positions.count([x,y])
                if num > 0:
                    file.write(f"{num}")
                else:
                    file.write(".")

                if x == width - 1:
                    file.write("\n")
    
    return "Printed positions to positions.txt"


def symmetry_check(positions):
    # find left and right robots
    left_robots, right_robots = [], []
    for position in positions:
        x, y = position[0], position[1]
        if x < int((width / 2) - 0.5):
            left_robots.append([x,y])
        if x >= int(width / 2 + 0.5):
            right_robots.append([x,y])

    if len(left_robots) == 0:
        return False

    # for every robot in quadrant 1 and 4 there needs to be a matching one in q2 or q3
    symmetrical = True
    for robot in left_robots:
        x, y = robot[0], robot[1]
        symmetrical_x = (width - 1) - x
        if [symmetrical_x, y] not in right_robots:
            symmetrical = False

    return symmetrical

print(symmetry_check(final_positions))

def longest_chain(positions):
    longest_chain = 0
    for position in positions:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        x, y = position[0], position[1]
        for dx, dy in directions:
            chain = 0 
            x, y = x + dx, y + dy
            while [x, y] in positions:
                chain += 1
                if chain > longest_chain:
                    longest_chain = chain
                x, y = x + dx, y + dy
    return longest_chain



robot_positions = []
should_continue = True
i = 0 
while(should_continue == True):
    robot_positions = []
    print(i)
    for robot in robots:
        robot[0], robot[1] = move(robot[0], robot[1], robot[2], robot[3])
        robot_positions.append([robot[0], robot[1]])
    # if symmetry_check(robot_positions):
    #     print(robot_positions)
    #     print("STOPPING")
    #     should_continue = False

    # find longest row / column
    if longest_chain(robot_positions) >= 7:
        should_continue = False
    i += 1

print(print_positions(robot_positions))
print(symmetry_check(robot_positions))