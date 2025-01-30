data_path = './day22_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')
#test_data = [1,10,100,2024]
test_data = [1,2,3,2024]

def get_next_secret(secret):
    # step 1
    mixer = secret * 64
    secret = mix(mixer, secret)
    secret = prune(secret)

    # step 2
    mixer = secret // 32
    secret = mix(mixer, secret)
    secret = prune(secret)

    # step 3
    mixer = secret * 2048
    secret = mix(mixer, secret)
    secret = prune(secret)

    return secret


def mix(mixer, secret):
    return mixer ^ secret

def prune(secret):
    return secret % 16777216


def find_nth_secret(n, secret):
    buyer_list = []
    for i in range(n):
        buyer_list.append(secret % 10)
        secret = get_next_secret(secret)
    return secret, buyer_list

total_1 = 0
part2_lists = []

for val in test_data:
    secret, buyer_list = find_nth_secret(2000, int(val))
    total_1 += secret
    part2_lists.append(buyer_list)


print("Part 1 Solution: ", total_1)

# part 2 plan 
# go through each list of secret numbers, create a dictionary for each new sequence
# within a single set of secret numbers, if we find a higher price for a certain sequence change the value
# now we need to go through all the highest sequence values for each list of secret numbers and add them up 
#    into a new total dictionary, the highest value in this will be the winner

all_maps = []

for list in part2_lists:
    map = dict()
    for i in range(4,2000):
        sequence = (list[i - 3] - list[i - 4], list[i - 2] - list[i - 3], list[i - 1] - list[i - 2], list[i] - list[i - 1])
        if sequence in map:
            if map[sequence] < list[i]:
                map[sequence] = list[i]
        map[sequence] = list[i]
    all_maps.append(map)

highest_value_map = dict()

for map in all_maps:
    for sequence, value in map.items():
        if sequence in highest_value_map:
            highest_value_map[sequence] += value
        else:
            highest_value_map[sequence] = value

highest_value = 0
highest_sequence = ()

for sequence, value in highest_value_map.items():
    if value > highest_value:
        highest_value = value
        highest_sequence = sequence

print(highest_sequence, highest_value)
print("Part 2 Solution = ", highest_value)