# https://adventofcode.com/2025/day/4

import numpy as np
import sys


def find_accessible(grid):
  dirs = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
  in_range = lambda y, x: 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]
  accessible_rolls = []
  for (y, x), v in np.ndenumerate(grid):
    if v != '@': continue
    count = 0
    for dy, dx in [(y+i, x+j) for i, j in dirs]:
      if in_range(dy, dx) and grid[dy, dx] == '@':
        count += 1
    if count < 4:
      accessible_rolls.append((y, x))
  return accessible_rolls


def part1(file):
  grid = np.genfromtxt(file, dtype=str, delimiter=1)
  return len(find_accessible(grid))


def part2(file):
  grid = np.genfromtxt(file, dtype=str, delimiter=1)
  total = 0
  while rolls := find_accessible(grid):
    total += len(rolls)
    for y, x in rolls:
      grid[y, x] = '.'
  return total


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
