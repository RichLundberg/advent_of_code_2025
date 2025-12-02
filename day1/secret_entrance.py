rotations = list()

with open("input.txt") as f:
  for line in f:
    multiplier = 1
    if line[0] == 'L':
        multiplier = -1
    rotation = multiplier * int(line[1:])
    rotations.append(rotation)

dial_value = 50
zeros = 0
passes = 0
for rotation in rotations:
    new_dial_value = (dial_value + rotation) % 100

    distance = abs(rotation)
    full_rotations = distance // 100
    rest = distance - full_rotations * 100

    passes += full_rotations
    if (dial_value > 0 and (rotation < 0 and rest > dial_value) or (rotation > 0 and rest + dial_value > 100)):
        passes += 1

    if new_dial_value == 0:
        zeros += 1

    dial_value = new_dial_value

print("zeros: ", zeros)
print("passes: ", passes)

print("RESULT: ", zeros + passes)