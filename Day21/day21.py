data_path = './day21_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

print(data)

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
    0: (1, 0),
    1: (0, 1),
    2: (1, 1),
    3: (2, 1),
    4: (0, 2),
    5: (1, 2),
    6: (2, 2),
    7: (0, 3),
    8: (1, 3),
    9: (2, 3),
    "A": (2,3)
}


directional = {
    "<": (0, 0),
    "v": (0, 0),
    "^": (0, 0),
    ">": (0, 0),
    "A": (0, 0),
}

