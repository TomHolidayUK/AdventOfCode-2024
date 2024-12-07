from itertools import product

data_path = './day7_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

n = 3  
combinations = [''.join(p) for p in product('01', repeat=n)]
print(combinations)


# Plan
# 1 - loop through data and for each line try every combination of addition and multiplication
#     to do this we will calculate the number of numbers
#     then use itertools.product
# 2 - add up all the valid results

total = 0

def possible_combinations(length):
    combinations = [''.join(p) for p in product('01', repeat=(length-1))]
    return combinations

for line in data:
    test_value, operators = line.split(":")
    print("test_value: ", test_value)
    operators_list = [int(num) for num in operators[1:].split(' ')]
    print("operators_list: ", operators_list)
    length = len(operators_list)
    combinations = possible_combinations(length)
    print("combinations: ", possible_combinations(length))
    for combination in combinations:
        combination_total = operators_list[0] 
        for i in range(1, length):
            if combination[i-1] == "1":
                combination_total *= operators_list[i]
            elif combination[i-1] == "0":
                combination_total += operators_list[i]
        print("for ", combination, " total = ", combination_total)

        if combination_total == int(test_value):
            print("combination ", combination, "works for ", test_value)
            total += int(test_value)
            break
    print("*********")


print("Part 1 Total Valid = ", total)

total2 = 0

def possible_combinations2(length):
    combinations = [''.join(p) for p in product('012', repeat=(length-1))]
    return combinations

def remove_specific_spaces(string, indexes_to_remove):
    removals = 0
    # go through string, when we reach an index to remove, remove it 
    string_list = list(string)

    for i, char in enumerate(string_list):
        if (i+removals) in indexes_to_remove:
            string_list.pop(i+removals)
            removals += 1

    new_string = ''.join(string_list)
    print("new_string - ", new_string)


print(remove_specific_spaces("6 8 6 15", [3, 5]))

# for line in data:
#     test_value, operators = line.split(":")
#     print("test_value: ", test_value)
#     operators_list = [int(num) for num in operators[1:].split(' ')]
#     print("operators_list: ", operators_list)
#     length = len(operators_list)
#     combinations = possible_combinations2(length)
#     print("combinations: ", possible_combinations2(length))
#     for combination in combinations:
#         success = False

#         if success:
#             print("found success, breaking")
#             break

#         combination_total = operators_list[0] 
#         # we need to see if there is a concat in the combination, if there is then we need to rewrite the operator list accodingly
#         if "2" in combination:
#             print("combination contains concat - ", combination)
#             # print("operators[1:]) before - ", operators[1:])
#             space_indexes = [i for i, c in enumerate(operators[1:]) if c == " "]
#             print("space_indexes - ", space_indexes)
#             indexes_to_remove = []
#             for i, char in enumerate(combination):
#                 if char == "2":
#                     indexes_to_remove.append(space_indexes[i])

#             print("indexes_to_remove - ", indexes_to_remove)

#             string_list = list(operators[1:])

#             # NOT REMOVING SPACES CORRECTLY !!!!
#             for index in indexes_to_remove:
#                 string_list.pop(index)
#             new_string = ''.join(string_list)
#             print("new_string - ", new_string)

#             # now we have a new operator string
#             # we also need to edit the combination to no longer include the concat because we've already processed i

#             new_combination = combination.replace("2", '')
#             print("new_combination - ", new_combination)


#         else:
#             for i in range(1, length):
#                 # # we need to check if the next combination is a concat, because the logic changes if it is 
#                 # if i < length - 1:
#                 #     if combination[i] == "2":
#                 #         print("next combination =  concat")
#                 if combination[i-1] == "2":
#                     combination_total *= operators_list[i]
#                 if combination[i-1] == "1":
#                     combination_total *= operators_list[i]
#                 elif combination[i-1] == "0":
#                     combination_total += operators_list[i]
#             print("for ", combination, " total = ", combination_total)

#             if combination_total == int(test_value):
#                 print("combination ", combination, "works for ", test_value)
#                 total2 += int(test_value)
#                 success = True
#                 break
#     print("*********")


print("Part 2 Total Valid = ", total2)