import time

data_path = './day17_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# Plan 
# Split data into registers and instruction-opcode pairs
# Write functions to calculate combo operand
# Write functions for each instruction
# Run instructions and record outputs

# Split data into registers and instruction-opcode pairs
register_string, instrucs = file_content.split('\n\n')

instruction_codes = instrucs.split(': ')[1].split(',')
instructions = []
for i in range(0, int(len(instruction_codes)), 2):
    instructions.append([int(instruction_codes[i]), int(instruction_codes[i + 1])])


# Increase function pointer by 2 until end of instructions 
def find_output(a,b,c):

    output = ""
    instruction_ptr = 0

    registers = {
        "A": a,
        "B": b,
        "C": c
    }

    # Write functions to calculate combo operand
    def combo_operand(instruction):
        if instruction >= 0 and instruction <= 3:
            return instruction
        if instruction == 4:
            return registers["A"]
        if instruction == 5:
            return registers["B"]
        if instruction == 6:
            return registers["C"]

    # Write functions for each instruction
    def adv(operand):
        # division
        result = int(registers["A"] / pow(2,combo_operand(operand)))
        #print("adv - setting A register to ", result)
        registers["A"] = result

    def bxl(operand):
        # bitwise XOR of register B and literl operand
        result = registers["B"] ^ operand
        #print("bxl - setting B register to ", result)
        registers["B"] = result

    def bst(operand):
        result = combo_operand(operand) % 8
        #print("bst - setting B register to ", result)
        registers["B"] = result

    def jnz(operand):
        nonlocal instruction_ptr 
        if registers["A"] == 0:
            return
        #print("jnz - setting instruction pointer to ", int(operand / 2))
        instruction_ptr = int(operand / 2)

    def bxc(operand):
        result = registers["B"] ^ registers["C"]
        #print("bxc - setting B register to ", result)
        registers["B"] = result

    def out(operand):
        nonlocal output
        result = combo_operand(operand) % 8
        #print("out - outputting ", result)
        if len(output) == 0:
            output += str(result)
        else:
            output += "," + str(result)

    def bdv(operand):
        result = int(registers["A"] / pow(2,combo_operand(operand)))
        #print("bdv - setting B register to ", result)
        registers["B"] = result

    def cdv(operand):
        result = int(registers["A"] / pow(2,combo_operand(operand)))
        #print("cdv - setting C register to ", result)
        registers["C"] = result

    while instruction_ptr <= len(instructions) - 1:
        instruction, operand = instructions[instruction_ptr][0], instructions[instruction_ptr][1]
        #print("processing ", instruction, operand)
        if instruction == 0:
            adv(operand)
        elif instruction == 1:
            bxl(operand)
        elif instruction == 2:
            bst(operand)
        elif instruction == 3:
            if registers["A"] == 0:
                instruction_ptr += 1
            else:
                jnz(operand)
                continue
        elif instruction == 4:
            bxc(operand)
        elif instruction == 5:
            out(operand)
        elif instruction == 6:
            bdv(operand)
        elif instruction == 7:
            cdv(operand)
        

        instruction_ptr += 1

    return output

print("Part 1 Solution = ", find_output(117440,0,0))

print("Part 1 Solution = ", find_output(40923545567988,0,0))
print("Part 1 Solution = ", find_output(60923545567988,0,0))
print("Part 1 Solution = ", find_output(80923545567988,0,0))
print("Part 1 Solution = ", find_output(90923545567988,0,0))
print("Part 1 Solution = ", find_output(110923545567988,0,0))
print("Part 1 Solution = ", find_output(130923545567988,0,0))
print("Part 1 Solution = ", find_output(160923545567988,0,0))
print("Part 1 Solution = ", find_output(180923545567988,0,0))
print("Part 1 Solution = ", find_output(140923545567988,0,0))
print("Part 1 Solution = ", find_output(160923545567988,0,0))
print("Part 1 Solution = ", find_output(184734789723847,0,0))

# should_continue = True
# val = 10923545567988

# while should_continue == True:
#     output = find_output(val,0,0)
#     print(val, output)
#     # time.sleep(0.5)
#     if output == "2,4,1,1,7,5,0,3,1,4,4,0,5,5,3,0": 
#         print(val)
#         should_continue = False
#         break
#     else:
#         val += 1

# print("Part 2 Solution = ", val)