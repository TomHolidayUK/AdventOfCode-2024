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
            print("Level not safe - changed from increasing to decreasing")
            is_safe = False
        if (initial_direction == "down" and int_array[i] > int_array[i - 1]):
            print("Level not safe - changed from decreasing to increasing")
            is_safe = False

        # check if increase or decrease by more than 3
        if ((int_array[i]-int_array[i - 1] > 3)):
            print("Level not safe - increase by more than 3")
            is_safe = False
        if ((int_array[i - 1]-int_array[i] > 3)):
            print("Level not safe - decrease by more than 3")
            is_safe = False

        # check if no change at all
        if (int_array[i] == int_array[i - 1]):
            print("Level not safe - no change")
            is_safe = False
    
    # if is_safe is still safe at this poitn then it really is safe
    if (is_safe):
        safe_total += 1

print("Part 1 Total = ", safe_total)