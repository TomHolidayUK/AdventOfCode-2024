data_path = './day24_data_test.txt'

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
        return map[val1] != map[val2]
    if func == "OR":
        return map[val1] ^ map[val2]

# while "" in final_wires:
for gate in all_gates_good:
    if map[gate[0]] and map[gate[2]]:
        print(gate[3], process(gate))
        map[gate[3]] = process(gate)



# print(final_wires)
    


