import sys

def count_matches1(grid, i, j):
  sum = 0
  width, height = len(grid[0]), len(grid)
  for x in range(-1, 2):
    for y in range(-1, 2):
      if x == y == 0: continue
      if i+x*3 < 0 or width <= i+x*3 or j+y*3 < 0 or height <= j+y*3: continue
      test_word = "".join([grid[i + x*c][j + y*c] for c in range(4)])
      if (test_word == "XMAS"): sum += 1
  return sum


def part1(file):
  with open(file) as input:
    grid = [line.rstrip() for line in input.readlines()]
    width, height = len(grid[0]), len(grid)
    return sum(count_matches1(grid, i, j)
               for i in range(width)
               for j in range(height))


def count_matches2(grid, i, j):
  if (grid[i][j] != 'A'): return 0
  c1, c2, c3, c4 = grid[i-1][j-1], grid[i+1][j+1], grid[i-1][j+1], grid[i+1][j-1]
  return 1 if ((c1=='M' and c2=='S') or (c1=='S' and c2=='M')) and ((c3=='M' and c4=='S') or (c3=='S' and c4=='M')) else 0


def part2(file):
  with open(file) as input:
    grid = [line.rstrip() for line in input.readlines()]
    width, height = len(grid[0]), len(grid)
    return sum(count_matches2(grid, i, j)
               for i in range(1, width - 1)
               for j in range(1, height - 1))


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
