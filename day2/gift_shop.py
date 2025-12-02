with open("input.txt") as f:
  ids = [id for id in f.read().split(",")]

invalids = 0
for id in ids:
  # leading 0
  start, end = id.split("-")
  if start[0] == '0' or end[0] == '0':
    invalids += 1
  else:
    for x in range(int(start), int(end) + 1):
      number_str = str(x)
      length = len(str(x))
      middle = length // 2

      for i in range(1, middle + 1):
        if length % i == 0:
          repeats = len(str(x)) // i
          all_same = True
          for j in range(1, repeats):
            if (number_str[:i] != number_str[i * j:i * (j + 1)]):
              all_same = False
          if all_same:
            invalids += x
            break

print("RESULT: ", invalids)
