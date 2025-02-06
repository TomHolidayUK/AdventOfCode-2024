data_path = './day23_data.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

data = file_content.split('\n')

# make a map of each connection to each node
# loop through all connections, for each node, loop through their map and see if there are any matches
# each match is a LAN party

all_conns = set()
lan_parties = set()
node_conns = dict()

for line in data:
    a,b = line.split("-")
    if a in node_conns and b not in node_conns[a]:
        node_conns[a].append(b)
    else:
        node_conns[a] = [b]
    
    if b in node_conns and a not in node_conns[b]:
        node_conns[b].append(a)
    else:
        node_conns[b] = [a]

def find_matches(a, b):
    return set(a) & set(b)

for line in data:
    a,b = line.split("-")
    matches = find_matches(node_conns[a], node_conns[b])
    for match in matches:
        # to avoid repetition sort
        sorted_conns = sorted([a,b,match])
        print(sorted_conns)
        lan_parties.add(tuple(sorted_conns))

# print(lan_parties)
# print(len(lan_parties))

part1_total = 0 

for party in lan_parties:
    if party[0][0] == "t" or party[1][0] == "t" or party[2][0] == "t":
        part1_total += 1


print("Part 1 Solution: ", part1_total)
