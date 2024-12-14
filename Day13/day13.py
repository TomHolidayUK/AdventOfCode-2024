import re

data_path = './day13_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Plan 
# Split data into claws with A, B and Prize data
# Work out if a claw is possible by trying all possible combination of A and B (10,000 for each - claw not too bad)
# Work out cheapest route 

# Split data into claws with A, B and Prize data
claws = file_content.split('\n')
print(claws)

all_data = [[]]
i = 0

for data_string in claws:
    button_data = []
    line = data_string.split('\n')
    if line != [""]:
        numbers = re.findall(r'\d+', line[0])  # \d+ matches one or more consecutive digits
        ints = [int(number) for number in numbers]
        all_data[i].append(ints)
    else:
        all_data.append([])
        i += 1

print(all_data)

total_cost = 0

# Work out if a claw is possible by trying all possible combination of A and B (10,000 for each - claw not too bad)
for claw in all_data:
    buttonA = claw[0]
    buttonB = claw[1]
    target = claw[2]

    x_combinations = []
    y_combinations = []
    possible_combinations = []

    for i in range(100):
        for j in range(100):
            # x
            if (buttonA[0] * i) + (buttonB[0] * j) == target[0]:
                print("[x] ", i, "+", j, "=", target[0])
                x_combinations.append([i,j])
            # y
            if (buttonA[1] * i) + (buttonB[1] * j) == target[1]:
                print("[y] ", i, "+", j, "=", target[1])
                y_combinations.append([i,j])

    for combi in x_combinations:
        if combi in y_combinations:
            possible_combinations.append(combi)

    print(possible_combinations)

    # Work out cheapest route 


    for combi in possible_combinations:
        cost = (3 * combi[0]) + (1 * combi[1])
        total_cost += cost
    print("-----")

print("Part 1 Answer = ", total_cost)



