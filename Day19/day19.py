data_path = './day19_data_test.txt'

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

for ptrn in desired_ptrns:
    size = len(ptrn)

    is_possible = True

    # we will use pointers to move through the disered pattern and compare to available patterns
    pos = 0
    combo = 0

    while pos < size:
        #ptrn_array = list(ptrn)
        char = (ptrn[pos])

        if char in available_ptrns:
            print(char, "available")
            pos += 1
        else:
            print(char, "UNavailable")
            should_continue = True
            while should_continue:

                if combo + pos > size:
                    print("at end")
                    is_possible = False
                    pos = size + 1
                    break

                combo += 1
                start = pos
                end = start + combo
                chars = ptrn[start:end]
                if chars in available_ptrns:
                    print(chars, "available")
                    should_continue = False
                    pos = end

    if is_possible:
        counter += 1
        print(ptrn, "is possible")
    else:
        print(ptrn, "is not possible")


ptrn = desired_ptrns[5]

# size = len(ptrn)

# # we will use pointers to move through the disered pattern and compare to available patterns
# pos = 0
# combo = 0

# while pos < size:
#     #ptrn_array = list(ptrn)
#     char = (ptrn[pos])

#     if char in available_ptrns:
#         print(char, "available")
#         pos += 1
#     else:
#         print(char, "UNavailable")
#         should_continue = True
#         while should_continue:

#             if combo + pos > size:
#                 print("at end")
#                 pos = size + 1
#                 break

#             combo += 1
#             start = pos
#             end = start + combo
#             chars = ptrn[start:end]
#             if chars in available_ptrns:
#                 print(chars, "available")
#                 should_continue = False
#                 pos = end


print("Part 1 Solution = ", counter)