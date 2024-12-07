data_path = './day5_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


# Plan
# 1 - split data into ordering rules and update order
# 2 - then go through the list of update orders, and as you iterate through, store previous numbers
#     and look for any rules assocaited with the current number
# 3 - if there is a rule for the current number that states that it needs to be before a number that
#     has appeared previously then this update is invalid
# 4 - store the valid updates and then find the middle integer of each one and add them up


# 1 - split data 

# ordering_rules_chars = []
# update_order_chars = []

# data = file_content.split('\n')
# after_break = False

# ordering_rules = []

# for line in data:
#     if line.strip() == "":
#         after_break = True
#     if after_break:
#         update_order_chars.append(line)
#     else:
#         ordering_rules_chars.append(line)

# update_order_chars.pop(0)

# for line in ordering_rules_chars:
#     int_list = [int(num) for num in line.split('|')]
#     ordering_rules.append(int_list)

# print(ordering_rules)

# update_order = []

# for line in update_order_chars:
#     int_list = [int(num) for num in line.split(',')]
#     update_order.append(int_list)

# print(update_order)


# 1 - split data (chatgpt solution - my solution is the one above but i like the splitting and list comprehension of the solution below)
# (going forward i will try to imiplement split and list comprehension)
data = file_content.split('\n')
split_index = data.index("")  # Find the index of the empty line
ordering_rules_chars = data[:split_index]
update_order_chars = data[split_index + 1:]

ordering_rules = [[int(num) for num in line.split('|')] for line in ordering_rules_chars]

update_order = [[int(num) for num in line.split(',')] for line in update_order_chars]

print(ordering_rules)
print(update_order)

# 2 - go through data 

def find_relevant_rules(int):
    return [x for x in ordering_rules if x[0] == int]

total_updates = 0
valid_updates = []
invalid_updates = []

for update in update_order:
    previous_values = []
    valid = True
    for num in update:
        if valid == False:
            break
        relevant_rules = find_relevant_rules(num)
        # check if there are any relevant_rules that contain a previous value
        for rule in relevant_rules:
            if rule[1] in previous_values:
                #print("update invalid because of: ", num, " and ", rule)
                valid = False
                invalid_updates.append(update)
                break
        previous_values.append(num)
    if valid:
        total_updates += 1
        valid_updates.append(update)
    

print("Part 1 Total Valid = ", len(valid_updates))

total = 0

# all updates have an odd number of numbers 

for update in valid_updates:
    middle_index = (len(update) - 1) / 2
    middle_value = update[int(middle_index)]
    total += middle_value

print("Part 1 Solution = ", total)

total2 = 0

# Part 2 plan 


# go through invalid updates, if there is an invalid number, move it left and try again
# when valid, find middle value

def check_update(update_row):
    previous_values = []
    for index, num in enumerate(update_row):
        relevant_rules = find_relevant_rules(num)
        for rule in relevant_rules:
            if rule[1] in previous_values:
                return index
        previous_values.append(num)
    return -1

final_updates = []

for update in invalid_updates:
    result = check_update(update)
    while result > 0:
        update[result], update[result - 1] = update[result - 1], update[result]
        result = check_update(update)
    final_updates.append(update)
        
for update in final_updates:
    middle_index = (len(update) - 1) / 2
    middle_value = update[int(middle_index)]
    total2 += middle_value


print("Part 2 Solution = ", total2)


        