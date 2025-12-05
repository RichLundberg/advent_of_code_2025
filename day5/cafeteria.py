with open("input.txt") as f:
  input = [x.strip().split("\n") for x in f.read().split("\n\n")]

fresh_ingredients = 0
fresh_ingredient_ids = 0
fresh_ingredient_list = list()

for sequence in input[0]:
  start, end = [int(x) for x in sequence.split("-")]
  fresh_ingredient_list.append((start, end))

###### Excercise 1 ######
for ingredient in input[1]:
  ingredient = int(ingredient)
  for start, end in fresh_ingredient_list:
    if ingredient >= start and ingredient <= end:
      fresh_ingredients += 1
      break

###### Excercise 2 ######
for i in range(len(fresh_ingredient_list)):
  for j, (x, y) in enumerate(fresh_ingredient_list):
    if i != j:
      start, end = fresh_ingredient_list[i]

      start_in_range = (x <= start <= y)
      end_in_range = (x <= end <= y)

      if start_in_range and end_in_range:
        fresh_ingredient_list[i] = (-1, -1)

      elif start_in_range and not end_in_range:
        fresh_ingredient_list[i] = (y + 1, end)

      elif end_in_range and not start_in_range:
        fresh_ingredient_list[i] = (start, x - 1)

for x, y in fresh_ingredient_list:
  if x != -1 and y != -1:
    fresh_ingredient_ids += y - x + 1

print("Number of fresh ingredients: ", fresh_ingredients)
print("Number of total fresh ingredient IDs: ", fresh_ingredient_ids)