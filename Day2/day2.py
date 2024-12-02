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

# for lvl in data:
#     chars = lvl.split()
#     int_array = [int(char) for char in chars]
#     direction = None 
#     level_error_count = 0
#     up_count = 0
#     down_count = 0
#     for i in range(1, len(int_array)):
#         # work out if level tends up or down
#         if (int_array[i] > int_array[i - 1]):
#             up_count += 1
#         elif (int_array[i] < int_array[i - 1]):
#             down_count += 1

#     if (up_count > down_count):
#         direction = "up"
#     elif (up_count < down_count):
#         direction = "down"
#     else:
#         level_error_count += 3

#     for i in range(1, len(int_array)):

#         # this time we are going to count the errors on each level, if there are more than 1 errors the level is unsafe
        
#         # change in direction
#         if (i < len(int_array) - 1):
#             if (direction == "up" and (int_array[i] > int_array[i - 1]) and (int_array[i + 1] < int_array[i]) and ((int_array[i + 1] - int_array[i - 1]) < 3)):
#                 print("up and down")
#                 level_error_count -= 2
#             if (direction == "down" and (int_array[i] < int_array[i - 1]) and (int_array[i +1 ] > int_array[i]) and ((int_array[i - 1] - int_array[i + 1]) < 3)):
#                 print("down and up")
#                 level_error_count -= 2

#         if (direction == "up" and int_array[i] < int_array[i - 1]):
#             print("Level not safe - changed from increasing to decreasing")
#             level_error_count += 1
#         if (direction == "down" and int_array[i] > int_array[i - 1]):
#             print("Level not safe - changed from decreasing to increasing")
#             level_error_count += 1

#         if (i < len(int_array) - 1):
#             if (direction == "up" and (int_array[i] - int_array[i - 1] > 3) and (int_array[i] - int_array[i + 1] > 3) and ((int_array[i + 1] - int_array[i - 1]) < 3)):
#                 print("more than 3 correction (up-2)")
#                 level_error_count -= 2
#             if (direction == "up" and (int_array[i] - int_array[i - 1] > 3) and (int_array[i] - int_array[i + 1] <= 3) and ((int_array[i + 1] - int_array[i - 1]) < 3)):
#                 print("more than 3 correction (up-1)")
#                 level_error_count -= 1
#             if (direction == "down" and (int_array[i] - int_array[i - 1] > 3) and (int_array[i] - int_array[i + 1] > 3) and ((int_array[i + 1] - int_array[i - 1]) < 3)):
#                 print("more than 3 correction (down-2)")
#                 level_error_count -= 2
#             if (direction == "down" and (int_array[i] - int_array[i - 1] > 3) and (int_array[i] - int_array[i + 1] <= 3) and ((int_array[i + 1] - int_array[i - 1]) < 3)):
#                 print("more than 3 correction (down-1)")
#                 level_error_count -= 1

#         # check if increase or decrease by more than 3 - in this case the level will NEVER be possible so add 2
#         if ((int_array[i]-int_array[i - 1] > 3)):
#             print("Level not safe - increase by more than 3")
#             if (i == 1 or i == len(int_array) - 1):
#                 level_error_count += 1
#             else:
#                 level_error_count += 3
#         if ((int_array[i - 1]-int_array[i] > 3)):
#             print("Level not safe - decrease by more than 3")
#             if (i == 1 or i == len(int_array) - 1):
#                 level_error_count += 1
#             else:
#                 level_error_count += 3

#         # check if no change at all
#         if (int_array[i] == int_array[i - 1]):
#             print("Level not safe - no change")
#             level_error_count += 1
    
#     # if is_safe is still safe at this poitn then it really is safe
#     if (level_error_count < 2):
#         safe_total2 += 1
#         #print("SAFE - ", level_error_count)
#     else:
#         print("UNSAFE - ", level_error_count)
#         print(direction)
#         print(int_array)
#         print("---------")

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
            print("Level not safe - changed from increasing to decreasing")
            return False
        if (direction == "down" and int_array[i] > int_array[i - 1]):
            print("Level not safe - changed from decreasing to increasing")
            return False

        # check if increase or decrease by more than 3 - in this case the level will NEVER be possible so add 2
        if ((int_array[i]-int_array[i - 1] > 3)):
            print("Level not safe - increase by more than 3")
            return False
        if ((int_array[i - 1]-int_array[i] > 3)):
            print("Level not safe - decrease by more than 3")
            return False

        # check if no change at all
        if (int_array[i] == int_array[i - 1]):
            print("Level not safe - no change")
            return False
        
    return True


for lvl in data:
    chars = lvl.split()
    int_array = [int(char) for char in chars]
    is_safe = True
    initial_direction = None 
    up_count = 0
    down_count = 0

    for i in range(1, len(int_array)):
        # work out if level tends up or down
        if (int_array[i] > int_array[i - 1]):
            up_count += 1
        elif (int_array[i] < int_array[i - 1]):
            down_count += 1

    if (up_count > down_count):
        direction = "up"
    elif (up_count < down_count):
        direction = "down"
    else:
        direction = "error"

    first_error_index = find_first_error_index(int_array, direction)

    if first_error_index is None:
        safe_total2 += 1
        continue
    else:
        int_array.pop(first_error_index)
        if is_safe_func(int_array, direction):
            safe_total2 += 1
            continue
            #print("SAFE")
        else:
            print("UNSAFE")
            print(int_array)
            print("-----")
    
    # print("-----")


print("Part 2 Total = ", safe_total2)

# 327 - too low 
# 351 - too high
# 338 - too low
# 345 no

# [13, 13, 10, 11, 14, 11]
# Level not safe - no change

# 1 7 3 5 7 (up and down - up)
# 15 13 10 15 9 (up and down - down)
# 10 13 7 15 17 (down and up - up)
# 17 15 5 13 11 (down and up - down)
