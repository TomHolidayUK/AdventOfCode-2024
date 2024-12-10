data_path = './day9_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Part 1 Plan
# 1 - iterate through disk map and change to list that includes spaces and id numbers
# 2 - reverse iterate through the new string moving file blocks into spaces until there are no spaces left
# 3 - convert to ints using list comprehension and perform checksum evaluation

# 1
disk_list = []
id_number = 0

for i,char in enumerate(file_content):
    if (i % 2 == 0):
        # print("block - ", int(char), " - ", str(id_number))
        # disk_list.append(int(char) * str(id_number))
        for j in range(int(char)):
            disk_list.append(id_number)
        id_number += 1
    else:
        # print("space")#
        for j in range(int(char)):
            disk_list.append(".")

print(disk_list)

disk_list_copy = disk_list[:]

# 3
length = len(disk_list)
index = length - 1

def contains_space(list):
    return "." in list

def edit_list(list, new_char, index):
    list[index] = new_char
    return list

while contains_space(disk_list):
    index_to_fill = disk_list.index(".")
    block_to_move = disk_list[index]
    # print("index_to_fill - ", index_to_fill)
    # print("block_to_move - ", block_to_move)
    edit_list(disk_list, block_to_move,  index_to_fill)
    disk_list.pop(index)
    # print("new disk_list - ", disk_list)
    # print(index)
    index -= 1

# 4 
int_conversion = [int(item) for item in disk_list]
#print(int_conversion)
print("length 2 = ", len(int_conversion))


part_1_total = 0 

for i, num in enumerate(int_conversion):
    part_1_total += i * num

print("Part 1 Answer = ", part_1_total)

# Part 2 Plan
# 4 - we need to represent the data differently, let's use a dictionary 
#     blocks will have a key "B" and spaces will have a key that represent's the amount of empty space left
#     dictionaries are ordered so we can reverse iterate through them 
# 5 - as we reverse iterate through we will find the earliest possible space for a block
# 6 - if no suitable space exists nothing happens and we move on 
# 7 - as we move blocks if empty space is left on the end, delete it
# 8 - if we move a block that is not on the end we need to replace it with empty space and join blocks around it 
# 9 - only move blocks to the left


# Part 2 Plan
# use 2 pointers approach

p1 = 0 
p2 = len(disk_list_copy) - 1

def find_required_space(list, size, block_start):
    count = 0
    # iterate throgh the whole pattern, but only up to the point of the current block as spaces after are invalid
    for i in range(block_start):
        if list[i] == ".":
            count += 1
        else:
            count = 0
        
        if count == size:
            return i - size + 1  
    return -1


print(disk_list_copy)

while p2 >= 0:
    # if space, continue. We are only interested in blocks 
    if disk_list_copy[p2] == ".":
        p2 -= 1
        continue

    # find block of this value
    value = disk_list_copy[p2]
    p3 = p2
    while disk_list_copy[p3] == value:
        p3 -= 1
    block_size = p2 - p3

    # p3 = pointer to the first position before the start of the blocl

    # so now we need to find the first available space for a block of size block_size
    # this space also needs to be to the left of the block (p3)
    space_index = find_required_space(disk_list_copy, block_size, p3 + 1)
    if space_index == -1:
        p2 -= block_size
        continue

    # now we have the space we need to do the move
    for space in range(space_index, space_index + block_size):
        disk_list_copy[space] = value

    # if block was at the end of the list, delete it 
    if p2 == len(disk_list_copy) - 1:
        disk_list_copy = disk_list_copy[:-block_size]
        p2 -= block_size
        continue
    else:
        # if it is not at the end, replace with spaces
        for index in range(p3 + 1, p2 + 1):
            disk_list_copy[index] = "."
        p2 -= block_size
        continue

print(disk_list_copy)

part_2_total = 0 

for i, num in enumerate(disk_list_copy):
    if num != ".":
        part_2_total += i * int(num)

print("Part 2 Answer = ", part_2_total)
