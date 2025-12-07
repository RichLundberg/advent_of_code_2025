puzzle_input = list()
with open("input.txt") as f:
    for line in f:
        puzzle_input.append(line.rstrip())

dynamic_table = dict()
def recursion(puzzle_input, beam, index):
    if index == len(puzzle_input) - 1:
        return 1

    else:
        for i, char in enumerate(puzzle_input[index]):
            if char == 'S' or (char == '.' and i == beam):
                return recursion(puzzle_input, i, index + 1)
            elif char == '^' and i == beam:
                if (beam, index) in dynamic_table:
                    return dynamic_table[(beam, index)]
                else:
                    left = recursion(puzzle_input, i - 1, index + 1)
                    right = recursion(puzzle_input, i + 1, index + 1)
                    dynamic_table[(beam, index)] = left + right
                    return left + right

timelines = recursion(puzzle_input, -1, 0)
print("Number of timelines: ", timelines)