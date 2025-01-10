from functools import cache

data_path = './day19_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()


# Plan 
# loop through desired designs
# loop through colours of desired design and try to find in available patterns
# if doesn't exist, increase size until found or until at the end of the desired design

available_patterns, desired_patterns = file_content.split("\n\n")

available_ptrns = available_patterns.split(", ")
desired_ptrns = desired_patterns.split("\n")


def is_pattern_possible(pattern):
    size = len(pattern)
    max_len = max(map(len, available_ptrns))

    is_possible = True

    # we will use pointers to move through the disered pattern and compare to available patterns
    pos_start = 0
    pos_end = 1
    high = 0

    while pos_end < size + 1:
        char = (pattern[pos_start:pos_end])

        if char in available_ptrns:
            #print(char, "available")
            high = pos_end + 1
            pos_start += len(char)
            pos_end = pos_start + 1
            is_possible = True
        else:
            #print(char, "UNavailable")
            pos_end += 1
            if (pos_end - pos_start > max_len):
                #print("reset - ", high)
                # try going backwards???
                if (pos_start > 0):
                    pos_end -= 2
                    pos_start -= 1
                is_possible = False

            is_possible = False
            

    if is_possible:
        print(pattern, "is possible")
        return True
    else:
        print(pattern, "is not possible")
        return False



counter = 0
for ptrn in desired_ptrns:
    if is_pattern_possible(ptrn):
        counter += 1
print("Part 1 Solution = ", counter)


# 338 - too high


# COULDN'T GET THIS SOLUTION WORKING SO INSTEAD LOOKED ONLINE AND FOUND THE SOLUTION BELOW




available_patterns, desired_patterns = file_content.split("\n\n")

patterns = available_patterns.split(", ")
maxlen = max(map(len, patterns))
desired_ptrns = desired_patterns.split("\n")


# we want to go through the desired patterns char by char
# once we find a available pattern to fit the first x chars, those chars are sorted and we move on to try to find the next x chars
# memoization with @cache to remember previous calculations to avoid repetition
@cache
def can_obtain(design):
    if design == "":
        # at end of design
        return True
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns and can_obtain(design[i:]):
            return True
    return False


@cache
def number_of_possibilities(design):
    if design == "":
        return 1
    count = 0 
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns:
            count += number_of_possibilities(design[i:])
    return count
    
counter = 0
counter2 = 0 


for design in desired_ptrns:
    if can_obtain(design):
        counter += 1
    counter2 += number_of_possibilities(design)


print("Part 1 Solution: ", counter)
print("Part 2 Solution: ", counter2)



# uuwwwrgrbgrwrwgruuurbwbggwwgbbrwbbuwrrrwrgrgbbwbubrgrrg
# ugwwbbwwruguwbbuurbggubwwbrurrrubbwwgbbrrrwbgugwbwuubrggrg


