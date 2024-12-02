data_path = './day2_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# iterate through levels and count how many are safe

safe_total = 0

for lvl in data:
    chars = lvl.split()
    int_array = [int(char) for char in chars]
    is_safe = True
    initial_direction = None 
    for i in range(1, len(int_array)):
        # work out if initial direction is up or down
        if (i == 1 and int_array[i] > int_array[i - 1]):
            initial_direction = "up"
        elif (i == 1 and int_array[i] < int_array[i - 1]):
            initial_direction = "down"
        
        # check if there is a change in direction
        if (initial_direction == "up" and int_array[i] < int_array[i - 1]):
            is_safe = False
        if (initial_direction == "down" and int_array[i] > int_array[i - 1]):
            is_safe = False

        # check if increase or decrease by more than 3
        if ((int_array[i]-int_array[i - 1] > 3)):
            is_safe = False
        if ((int_array[i - 1]-int_array[i] > 3)):
            is_safe = False

        # check if no change at all
        if (int_array[i] == int_array[i - 1]):
            is_safe = False
    
    # if is_safe is still safe at this poitn then it really is safe
    if (is_safe):
        safe_total += 1

print("Part 1 Total = ", safe_total)

safe_total2 = 0

def find_first_error_index(int_array, direction):
    for i in range(1, len(int_array)):        
        # check if there is a change in direction
        if (direction == "up" and int_array[i] < int_array[i - 1]):
            return i
        if (direction == "down" and int_array[i] > int_array[i - 1]):
            return i

        # check if increase or decrease by more than 3
        if ((int_array[i]-int_array[i - 1] > 3)):
            return i
        if ((int_array[i - 1]-int_array[i] > 3)):
            return i

        # check if no change at all
        if (int_array[i] == int_array[i - 1]):
            return i
        
def is_safe_func(int_array, direction):
    for i in range(1, len(int_array)):
        if (direction == "up" and int_array[i] < int_array[i - 1]):
            return False
        if (direction == "down" and int_array[i] > int_array[i - 1]):
            return False
        
        # check if increase or decrease by more than 3 - in this case the level will NEVER be possible so add 2
        if ((int_array[i]-int_array[i - 1] > 3)):
            return False
        if ((int_array[i - 1]-int_array[i] > 3)):
            return False

        # check if no change at all
        if (int_array[i] == int_array[i - 1]):
            return False
        
    return True

def direction_tendency(array):
    up_count = 0 
    down_count = 0 

    for i in range(1, len(int_array)):
        if (int_array[i] > int_array[i - 1]):
            up_count += 1
        elif (int_array[i] < int_array[i - 1]):
            down_count += 1

    if (up_count > down_count):
        return "up"
    elif (up_count < down_count):
        return "down"
    else:
        return "error"

for lvl in data:
    chars = lvl.split()
    int_array = [int(char) for char in chars]
    initial_direction = None 

    # work out if level tends up or down
    direction = direction_tendency(int_array)

    if direction is not "error":
        for i in range(len(int_array)):
            new_array = int_array[:i] + int_array[i + 1:]
            if (is_safe_func(new_array, direction)):
                safe_total2 += 1
                break

print("Part 2 Total = ", safe_total2)


