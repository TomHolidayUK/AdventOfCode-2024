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
        #print("left")
        new_x += width
    if new_y < 0:
        #print("top")
        new_y += height
    if new_x > width - 1:
        #print("right")
        new_x -= width
    if new_y > height - 1:
        #print("bottom")
        new_y -= height

    return new_x, new_y


# print(move(5,1,2,-3))

final_positions = []

# Apply move function to each robot 100 times
for robot in robots:
    x, y = robot[0], robot[1]
    for i in range(100):
        x, y = move(x, y, robot[2], robot[3])
    final_positions.append([x, y])

print(final_positions)

# Work out which robot is in which quadrant
q1, q2, q3, q4 = 0, 0, 0, 0
for position in final_positions:
    print(position)
    x, y = position[0], position[1]
    print(int(width / 2 - 0.5))
    print(int(height / 2 - 0.5))
    print(int((width - 1)/ 2 + 0.5))
    print(int(height / 2 + 0.5))
    if x < int((width / 2) - 0.5) and y < int(height / 2 - 0.5):
        print("q1")
        q1 += 1
    if x >= int(width / 2 + 0.5) and y < int(height / 2 - 0.5):
        print("q2")
        q2 += 1
    if x >= int(width / 2 + 0.5) and y >= int(height / 2 + 0.5):
        print("q3")
        q3 += 1
    if x < int(width / 2 - 0.5) and y >= int(height / 2 + 0.5):
        print("q4")
        q4 += 1

print(q1, q2, q3, q4)

print("Part 1 Total = ", q1 * q2 * q3 * q4)