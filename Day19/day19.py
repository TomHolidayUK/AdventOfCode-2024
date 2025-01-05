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

# print(available_ptrns)
# print(desired_ptrns)

# counter = 0

# def is_pattern_possible(pattern):
#     size = len(pattern)

#     is_possible = True

#     # we will use pointers to move through the disered pattern and compare to available patterns
#     pos = 0

#     while pos < size:
#         char = (pattern[pos])

#         if char in available_ptrns:
#             #print(char, "available")
#             pos += 1
#         else:
#             #print(char, "UNavailable")

#             is_possible = False
            
#             left = pos
#             right = size - pos - 1

#             for i in range(left + 1):
#                 for j in range(right + 1):
#                     chars = pattern[pos - i : pos + j + 1]
#                     #print(chars)
#                     if chars in available_ptrns:
#                         #print(chars, "available")
#                         is_possible = True
#                         # pos = pos + j + 1
#                         pos += 1
#                         break

#             if is_possible == False:
#                 #print("no possible combination to get", char)
#                 break


#     if is_possible:
#         print(pattern, "is possible")
#         return True
#     else:
#         print(pattern, "is not possible")
#         return False



import re

def find_all_indices_regex(haystack, needle):
    return [match.start() for match in re.finditer(re.escape(needle), haystack)]


def is_pattern_possible2(pattern):
    size = len(pattern)

    possible = False

    char_suitablity = [False] * size

    for ptrn in available_ptrns:
        if all(char_suitablity):
            print("at end - possible")
            possible = True
            break
        indices = find_all_indices_regex(pattern, ptrn)
        length = len(ptrn)
        for index in reversed(indices):
            print(ptrn, index)
            for i in range(length):
                char_suitablity[index + i] = True
            print(char_suitablity)

    # if not possible:
    #     #print("not possible")

    return possible




    

#is_pattern_possible2(desired_ptrns[0])
print(is_pattern_possible2("uuwwwrgrbgrwrwgruuurbwbggwwgbbrwbbuwrrrwrgrgbbwbubrgrrg"))


# for ptrn in desired_ptrns:
#     if is_pattern_possible2(ptrn):
#         counter += 1


# print("Part 1 Solution = ", counter)


# # 338 - too high




# available_patterns, desired_patterns = file_content.split("\n\n")

# patterns = available_patterns.split(", ")
# maxlen = max(map(len, patterns))
# desired_ptrns = desired_patterns.split("\n")

# @cache
# def can_obtain(design):
#     if design == "":
#         return True
#     for i in range(min(len(design), maxlen) + 1):
#         if design[:i] in patterns and can_obtain(design[i:]):
#             return True
#     return False
    
# print(sum(1 if can_obtain(design) else 0 for design in desired_ptrns))

# counter = 0 
# counter2 = 0 

# for design in desired_ptrns:
#     # if can_obtain(design):
#     #     counter += 1
#     # if is_pattern_possible2(design):
#     #     counter2 += 1
#     if can_obtain(design) != is_pattern_possible2(design):
#         print(design)

# print(counter, counter2)



# uuwwwrgrbgrwrwgruuurbwbggwwgbbrwbbuwrrrwrgrgbbwbubrgrrg
# ugwwbbwwruguwbbuurbggubwwbrurrrubbwwgbbrrrwbgugwbwuubrggrg