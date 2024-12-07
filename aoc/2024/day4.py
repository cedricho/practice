import itertools
import sys


def construct_word(grid, x, y, dx, dy):
  if dx == dy == 0: return None
  width, height = len(grid[0]), len(grid)
  if 0 <= x+dx*3 < width and 0 <= y + dy * 3 < height:
    return "".join(grid[y + dy * c][x + dx * c] for c in range(4))
  else:
    return None


def count_matches1(grid, x, y):
  return sum(1 for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]) if construct_word(grid, x, y, dx, dy) == "XMAS")


def count_matches2(grid, i, j):
  if (grid[j][i] != 'A'): return 0
  c1, c2, c3, c4 = grid[j-1][i-1], grid[j+1][i+1], grid[j-1][i+1], grid[j+1][i-1]
  return 1 if ((c1=='M' and c2=='S') or (c1=='S' and c2=='M')) and ((c3=='M' and c4=='S') or (c3=='S' and c4=='M')) else 0


def part1(file):
  with open(file) as input:
    grid = [line.rstrip() for line in input]
    width, height = len(grid[0]), len(grid)
    return sum(count_matches1(grid, i, j)
               for i in range(width)
               for j in range(height))


def part2(file):
  with open(file) as input:
    grid = [line.rstrip() for line in input]
    width, height = len(grid[0]), len(grid)
    return sum(count_matches2(grid, i, j)
               for i in range(1, width - 1)
               for j in range(1, height - 1))


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
