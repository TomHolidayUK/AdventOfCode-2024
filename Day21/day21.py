data_path = './day21_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# Plan
# Need to define coordinate system and positions for numerical and directional keypad
# Need to record position of each robot
# We will work backwards from the numerical to me 
# For each directional we need a function that calculates the input needed to move from a certain location 
#      on a directional keyboard to another and to press it
# we also need to same for a directional onto a numerical


# numerical
# robot 1
# directional
# robot 2
# directional 
# robot 3
# directional
# me

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

numerical = {
    "0": [1, 0],
    "1": [0, 1],
    "2": [1, 1],
    "3": [2, 1],
    "4": [0, 2],
    "5": [1, 2],
    "6": [2, 2],
    "7": [0, 3],
    "8": [1, 3],
    "9": [2, 3],
    "A": [2, 0]
}

directional = {
    "<": [0, 0],
    "v": [1, 0],
    "^": [1, 1],
    ">": [2, 0],
    "A": [2, 1],
}

robot1 = directional["A"]

def numerical_move(start, end):
    position = start.copy()
    directions = ""
    while position != end:
        if position[1] < end[1]:
            position[1] += 1
            directions += "^"
            continue
        if position[0] < end[0]:
            position[0] += 1
            directions += ">"
            continue
        if position[1] > end[1]:
            position[1] -= 1
            directions += "v"
            continue
        if position[0] > end[0]:
            position[0] -= 1
            directions += "<"
            continue
    return directions


def directional_move(start, end):
    position = start.copy()
    directions = ""
    while position != end:
        if position[1] > end[1]:
            position[1] -= 1
            directions += "v"
            continue
        if position[0] < end[0]:
            position[0] += 1
            directions += ">"
            continue
        if position[1] < end[1]:
            position[1] += 1
            directions += "^"
            continue
        if position[0] > end[0]:
            position[0] -= 1
            directions += "<"
            continue
    return directions


def numerical_to_directional(chars):
    position = numerical["A"]
    output = ""
    for char in chars:
        output += numerical_move(position, numerical[char])
        output += "A"
        position = numerical[char]
    
    return output


def directional_to_directional(start, chars):
    position = start.copy()
    output = ""
    for char in chars:
        #print(char, position, directional[char])
        output += directional_move(position, directional[char])
        output += "A"
        position = directional[char]
    
    return output

def shortest_length(input):
    output1 = numerical_to_directional(input)
    output2 = directional_to_directional(directional["A"], output1)
    output3 = directional_to_directional(directional["A"], output2)
    print(output3)
    return len(output3)

def numeric_part(input):
    # remove leading zeros
    real_start = 0
    for i, char in enumerate(input):
        if char != "0":
            real_start = i
            break

    return int(input[real_start:-1])


print(shortest_length(data[4]))


total = 0

# for input in data:
#     print(shortest_length(input), numeric_part(input))
#     total += shortest_length(input) * numeric_part(input)

# print("Part 1 Solution = ", total)



