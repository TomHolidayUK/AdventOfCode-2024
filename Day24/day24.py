data_path = './day24_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

wires, gates = file_content.split('\n\n')

# plan 
# seperate initial wires from gates
# in gates find initial gates
# from initial gates perform BFS until we get all output wires
# fill map of output wires



all_wires = wires.split('\n')
initial_wires = dict()

for wire in all_wires:
    key = wire[:3]
    val = wire[5]
    initial_wires[key] = int(val)

initial_gates = []
all_gates = gates.split('\n')
all_gates_good = []
max_z = 0
map = dict()

for gate in all_gates:
    spaces = []
    for i, char in enumerate(gate):
        if char == " ":
            spaces.append(i)
    first_wire = gate[:spaces[0]]
    second_wire = gate[spaces[1]+1:spaces[2]]
    func = gate[spaces[0]+1:spaces[1]]
    end = gate[spaces[3]+1:]
    if end[0] == "z":
        if int(end[1:]) > max_z:
            max_z = int(end[1:])

    all_gates_good.append([first_wire, func, second_wire, end])

    if first_wire not in map:
        map[first_wire] = ""
    if second_wire not in map:
        map[second_wire] = ""
    
    if (first_wire[0] == "x" or first_wire[0] == "y") and (second_wire[0] == "x" or second_wire[0] == "y"):
        initial_gates.append([first_wire, func, second_wire, end])
        map[first_wire] = initial_wires[first_wire]
        map[second_wire] = initial_wires[second_wire]


final_wires = []

for i in range(max_z + 1):
    final_wires.append("")

#print(map)

def process(values):
    val1 = values[0]
    val2 = values[2]
    func = values[1]
    
    if func == "AND":
        return map[val1] & map[val2]
    if func == "XOR":
        if map[val1] != map[val2]:
            return 1
        else:
            return 0
    if func == "OR":
        if map[val1] == 1 or map[val2] == 1:
            return 1
        else:
            return 0
    
print(map)

while "" in final_wires:
    for gate in all_gates_good:
        if map[gate[0]] != "" and map[gate[2]] != "":
            print(gate[0], gate[2], gate[3], process(gate))
            map[gate[3]] = process(gate)
            if gate[3][0] == "z":
                print("found z: ", int(gate[3][1:3]))
                final_wires[int(gate[3][1:3])] = process(gate)

    print("------")

print(map)
print(final_wires)

binary_number = ""
for i in range(max_z, -1, -1):
    binary_number += str(final_wires[i])

print("Part 1 result: ", int(binary_number, 2))
    


