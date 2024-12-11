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

print(stones)

def split(stone):
    print(stone)
    stone_string = str(stone)
    length = len(str(stone))
    print("length: ", length)
    split_index = length // 2
    stone1 = stone_string[:split_index]
    stone2 = stone_string[split_index:]
    print("stone1: ", stone1)
    print("stone2: ", stone2)
    return stone1, stone2

def blink(stones):
    for i, stone in enumerate(stones):
        if stone == 0:
            stone = 1
        elif len(str(stone)) % 2 == 0:
            print("split")
            stone1, stone2 = split(stone)
            print(stone1, stone2)
            stones.pop(i)
            print(stones)
            stones.insert(i, stone2)
            print(stones)
            stones.insert(i, stone1)
        else:
            print("2024")
            stone *= 2024
    print("FINAL STONES: ", stones)
    return stones


for i in range(2):
    stones = blink(stones)
    print(stones)