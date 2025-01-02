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

print(available_ptrns)
print(desired_ptrns)

counter = 0

def is_pattern_possible(pattern):
    size = len(pattern)

    is_possible = True

    # we will use pointers to move through the disered pattern and compare to available patterns
    pos = 0

    while pos < size:
        char = (pattern[pos])

        if char in available_ptrns:
            #print(char, "available")
            pos += 1
        else:
            #print(char, "UNavailable")

            is_possible = False
            
            left = pos
            right = size - pos - 1

            for i in range(left + 1):
                for j in range(right + 1):
                    chars = pattern[pos - i : pos + j + 1]
                    #print(chars)
                    if chars in available_ptrns:
                        #print(chars, "available")
                        is_possible = True
                        # pos = pos + j + 1
                        pos += 1
                        break

            if is_possible == False:
                #print("no possible combination to get", char)
                break


    if is_possible:
        print(pattern, "is possible")
        return True
    else:
        print(pattern, "is not possible")
        return False


# is_pattern_possible(desired_ptrns[4])


for ptrn in desired_ptrns:
    if is_pattern_possible(ptrn):
        counter += 1



print("Part 1 Solution = ", counter)


# 338 - too high