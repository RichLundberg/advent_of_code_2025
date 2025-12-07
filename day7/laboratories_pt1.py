beams = set()

puzzle_input = list()
with open("input.txt") as f:
    for line in f:
        puzzle_input.append(line)

splits = 0
for i, line in enumerate(puzzle_input):
    new_beams = set()
    row = list(line)
    for j, char in enumerate(row):
        if char == 'S':
            new_beams.add(j)

        elif char == '^' and j in beams:
            row[j + 1] = '|'
            row[j - 1] = '|'
            new_beams.add(j - 1)
            new_beams.add(j + 1)
            splits += 1

        elif char == '.' and j in beams:
            row[j] = '|'
            new_beams.add(j)

    beams = new_beams
    print("".join(row))
print("Number of splits: ", splits)