def calc(numbers, operator):
  result = int(numbers[0])
  for x in range(len(numbers) - 1):
    result = eval(str(result) + operator + numbers[x + 1])
  return result

longest_line = 0
input = list()
with open("input.txt") as f:
  for line in f:
    line = [x for x in line.rstrip()]
    input.append(line)
    if len(line) > longest_line:
        longest_line = len(line)

operators = {'*',  '+'}
numbers = list()
total = 0

for i in range(longest_line):
  number = ""
  for j in range(len(input)):
    if i < len(input[j]):
      char = input[j][i]
      if char in operators:
        operator = char
      elif char != ' ':
        number += input[j][i]

  if not number:
    total += calc(numbers, operator)
    numbers = []
  else:
    numbers.append(number)

total += calc(numbers, operator)

print("Grand total: ", total)