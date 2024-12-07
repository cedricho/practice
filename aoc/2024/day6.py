import copy
import itertools
import sys

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def find_guard(grid):
  for y, row in enumerate(grid):
    if '^' in row: return (row.index('^'), y)


def step(grid, x, y):
  width, height = len(grid[0]), len(grid)
  dir = 0
  while True:
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]
    if not (0 <= nx < width and 0 <= ny < height): return
    elif grid[ny][nx] == '#':
      dir = (dir + 1) % len(dirs)
      yield x, y, dir
    else:
      x, y = nx, ny
      yield x, y, dir


def has_loop(grid, x, y):
  s = step(grid, x, y)
  paths = set()
  paths.add((x, y, 0)) # guard initial position.
  while True:
    result = next(s, None)
    if not result: return False
    if result in paths:
      return True
    paths.add(result)


def part1(file):
  with open(file) as input:
    grid = [list(line.rstrip()) for line in input]
    x, y = find_guard(grid)
    return len(set((x, y) for x, y, dir in step(grid, x, y)))


def part2(file):
  with open(file) as input:
    grid = [list(line.rstrip()) for line in input]
    x, y = find_guard(grid)
    candidates = set((x, y) for x, y, dir in step(grid, x, y))
    obsticales = 0
    for i, j in candidates:
      if i == x and j == y: continue # ignore guard starting position
      grid[j][i] = '#'
      if has_loop(grid, x, y): obsticales += 1
      grid[j][i] = '.'
    return obsticales


print("Part 1:", part1(sys.argv[1]))
print("Part 1:", part2(sys.argv[1]))
