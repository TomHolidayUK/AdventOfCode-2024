data_path = './day9_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Part 1 Plan
# 1 - iterate through disk map and change to string that includes spaces and id numbers
# 2 - change to list because stirngs are immutable and we are going to be making lots of changes
# 3 - reverse iterate through the new string moving file blocks into spaces until there are no spaces left
# 4 - convert to ints using list comprehension and perform checksum evaluation

# 1
disk_string = ""
id_number = 0

for i,char in enumerate(file_content):
    if (i % 2 == 0):
        # print("block - ", int(char), " - ", str(id_number))
        disk_string += (int(char) * str(id_number))
        id_number += 1
    else:
        # print("space")
        disk_string += (int(char) * ".")

print(disk_string)

# 2
disk_list = list(disk_string)

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
    print(index)
    index -= 1

# 4 
int_conversion = [int(item) for item in disk_list]
print(int_conversion)

part_1_total = 0 

for i,num in enumerate(int_conversion):
    part_1_total += i * num

print("Part 1 Answer = ", part_1_total)
