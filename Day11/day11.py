data_path = './day11_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content

# Rules
# 0 -> 1
# even number of digits -> splits (remove leading zeros)
# else: * 2024

# Plan
# 1 - turn data into list so it's mutable
# 2 - make a function called blink which iterates through the stones and applies the rules
# 3 - apply the function recursively 25 times