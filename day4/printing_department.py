grid = list()
with open("input.txt") as f:
  for line in f:
    grid.append([entry for entry in line.strip()])

result = 0
col_length = len(grid)
removed_paper = True

while removed_paper:
  removed_paper = False
  for y, row in enumerate(grid):
    row_length = len(row)
    for x, entry in enumerate(row):
      if entry == '@':
        rolls_of_paper = 0
        for y_neighbor in range(y - 1, y + 2):
          for x_neighbor in range(x - 1, x + 2):
            if not (x_neighbor == x and y_neighbor == y):
              if (y_neighbor >= 0 and y_neighbor < col_length and x_neighbor >= 0 and x_neighbor < row_length):
                if grid[y_neighbor][x_neighbor] == '@':
                  rolls_of_paper += 1
        if rolls_of_paper < 4:
          grid[y][x] = 'x'
          result += 1
          removed_paper = True

print("RESULT: ", result)