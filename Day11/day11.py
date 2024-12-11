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

stones = [int(item) for item in data.split(" ")]
stones_copy = stones.copy()

# print(stones)

def split(stone):
    stone_string = str(stone)
    length = len(str(stone))
    split_index = length // 2
    stone1 = int(stone_string[:split_index])
    stone2 = int(stone_string[split_index:])
    return stone1, stone2

def blink(stones):
    # create a copy of the original which will be what we edit
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone1, stone2 = split(stone)
            new_stones.append(stone1)
            new_stones.append(stone2)
        else:
            new_stones.append(stone * 2024)
    return new_stones

for i in range(25):
    stones = blink(stones)

print("Part 1 Result = ", len(stones))

# Part 2 
# We only need to find the length, we don't need to calculate the stones, this is wasted calculation
# Do we use memoisation???

from functools import cache

@cache 
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[: length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    return count(stone * 2024, steps - 1)


print("Part 2 Result = ", sum(count(stone, 75) for stone in stones_copy))
