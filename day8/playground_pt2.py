puzzle_input = list()
circuits = list()

with open("input.txt") as f:
    for line in f:
        x,y,z = [int(x) for x in line.rstrip().split(",")]
        puzzle_input.append((x,y,z))
        circuits.append({(x,y,z)})

def euclidean_distance(j1, j2):
    x1, y1, z1 = j1
    x2, y2, z2 = j2
    return pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2)

distances = dict()
for i, junction_box1 in enumerate(puzzle_input):
    for j, junction_box2 in enumerate(puzzle_input[i + 1:]):
        distances[(i, j + i + 1)] = euclidean_distance(junction_box1, junction_box2)

distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}

total_circuits = len(circuits)
removed_circuits = 0
final_result = -1

for i, (best_pair, lowest_distance) in enumerate(distances.items()):

    a, b = best_pair
    coord_1 = puzzle_input[a]
    coord_2 = puzzle_input[b]

    for j, circuit in enumerate(circuits):
        if coord_1 in circuit:
            c1 = j
        if coord_2 in circuit:
            c2 = j

    if c1 != c2:
        circuits[c1] = circuits[c1].union(circuits[c2])
        circuits[c2] = {}
        removed_circuits += 1

    if removed_circuits == total_circuits - 1:
        x1, _, _ = coord_1
        x2, _, _ = coord_2
        final_result = x1 * x2
        break

print("Result: ", final_result)