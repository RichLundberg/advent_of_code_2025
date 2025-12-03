numbers = list()
with open("input.txt") as f:
  for line in f:
    numbers.append(line.strip())
result = 0
numbers_to_concat = 12 # 2

for number in numbers:
  largest = ""
  start = 0
  number_length = len(number)

  for i in range(numbers_to_concat):
    best_candidate = 0
    end = number_length - (numbers_to_concat - 1 - i)

    for j in range(start, end):
      if int(number[j]) > best_candidate:
        best_candidate = int(number[j])
        best_index = j

    start = best_index + 1
    largest += number[best_index]
  result += int(largest)

print("RESULT: ", result)