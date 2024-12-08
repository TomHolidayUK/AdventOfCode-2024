from itertools import product

data_path = './day7_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

n = 3  
combinations = [''.join(p) for p in product('01', repeat=n)]


# Plan
# 1 - loop through data and for each line try every combination of addition and multiplication
#     to do this we will calculate the number of numbers
#     then use itertools.product
# 2 - add up all the valid results

total = 0

def possible_combinations(length):
    combinations = [''.join(p) for p in product('01', repeat=(length-1))]
    return combinations

for i, line in enumerate(data):
    print("Part 1 Progress = ", i, "/", len(data))
    test_value, operators = line.split(":")
    #print("test_value: ", test_value)
    operators_list = [int(num) for num in operators[1:].split(' ')]
    #print("operators_list: ", operators_list)
    length = len(operators_list)
    combinations = possible_combinations(length)
    #print("combinations: ", possible_combinations(length))
    for combination in combinations:
        combination_total = operators_list[0] 
        for i in range(1, length):
            if combination[i-1] == "1":
                combination_total *= operators_list[i]
            elif combination[i-1] == "0":
                combination_total += operators_list[i]
        #print("for ", combination, " total = ", combination_total)

        if combination_total == int(test_value):
            #print("combination ", combination, "works for ", test_value)
            total += int(test_value)
            break
    #print("*********")


print("Part 1 Total Valid = ", total)

total2 = 0

def possible_combinations2(length):
    combinations = [''.join(p) for p in product('012', repeat=(length-1))]
    return combinations

for i, line in enumerate(data):
    print("Part 2 Progress = ", i, "/", len(data))
    test_value, operators = line.split(":")
    #print("test_value: ", test_value)
    operators_list = [int(num) for num in operators[1:].split(' ')]
    #print("operators_list: ", operators_list)
    length = len(operators_list)
    combinations = possible_combinations2(length)
    #print("combinations: ", possible_combinations2(length))
    for combination in combinations:
        combination_total = operators_list[0] 

        for i in range(1, length):
            if combination[i-1] == "2":
                combination_total = int(str(combination_total) + str(operators_list[i]))
            if combination[i-1] == "1":
                combination_total *= operators_list[i]
            elif combination[i-1] == "0":
                combination_total += operators_list[i]
        #print("for ", combination, " total = ", combination_total)

        if combination_total == int(test_value):
            #print("combination ", combination, "works for ", test_value)
            total2 += int(test_value)
            break
    #print("*********")


print("Part 2 Total Valid = ", total2)