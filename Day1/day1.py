import collections

data_path1 = './day1_data.txt'

with open(data_path1, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# make 2 arrays, one for each column of numbers

left = []
right = []
for el in data:
    numbers = el.split()
    left.append(int(numbers[0]))
    right.append(int(numbers[1]))


# order these arrays

sorted_left = sorted(left)
sorted_right = sorted(right)

# iterate through them and find the differences and add them up 

total = 0

for i in range(len(sorted_left)):
    dif = sorted_right[i] - sorted_left[i]
    total += abs(dif)

print("Part 1 Final Total: ", total)

# count frequency of numbers in the right column using the Counter class from collections

right_counter = collections.Counter(right)

total_2 = 0

for i in range(len(left)):
    total_2 += left[i] * right_counter[left[i]]

print("Part 2 Final Total: ", total_2)
