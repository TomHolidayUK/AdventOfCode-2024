import re

data_path = './day3_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, file_content)

total = 0

for numbers in matches:
    total += int(numbers[0]) * int(numbers[1])

print("Part 1 Solution = ", total)

total2 = 0

pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

dictionary = dict([])

indices_matches = re.finditer(pattern, file_content)
indices_do = re.finditer(pattern_do, file_content)
indices_dont = re.finditer(pattern_dont, file_content)

for index, match in enumerate(indices_matches):
    start_index = match.start()  
    dictionary[start_index] = int(matches[index][0]) * int(matches[index][1])

for index, match in enumerate(indices_do):
    start_index = match.start()  
    dictionary[start_index] = "do"

for index, match in enumerate(indices_dont):
    start_index = match.start()  
    dictionary[start_index] = "don't"

include = True

for key in sorted(dictionary.keys()):
    value = dictionary[key]
    if value == "do":
        include = True
    elif value == "don't":
        include = False
    if include and isinstance(value, int):
        total2 += value

print("Part 2 Solution = ", total2)