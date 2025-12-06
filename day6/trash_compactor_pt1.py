import re

input = list()
with open("input.txt") as f:
  for line in f:
   line = line.strip()
   input.append((re.sub(r'\s+', ' ', line)).split(" "))

total = 0
for i, value in enumerate(input[0]):
  result = int(value)
  operator = input[len(input) - 1][i]
  for j in range(len(input) - 2):
    expression = str(result) + operator + input[j + 1][i]
    result = eval(expression)
  total += result
print("Grand total: ", total)