from collections import deque
import numpy as np
import sys


def in_range(x, y, height, width):
  return 0 <= x < width and 0 <= y < height


def calc_path(grid, sx, sy, allowDup = False):
  peak = []
  q = deque()
  q.append((sx, sy))
  while q:
    x, y = q.pop()
    if grid[y, x] == 9: peak.append((x, y)); continue
    candidates = [(x + dx, y + dy) for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]]
    for cx, cy in candidates:
      if in_range(cx, cy, *grid.shape) and grid[cy, cx] == grid[y, x] + 1:
        q.append((cx, cy))
  return len(peak) if allowDup else len(set(peak))


with open(sys.argv[1]) as input:
  grid  = np.genfromtxt(input, delimiter=1)
  paths = sum([calc_path(grid, x, y) for (y, x), v in np.ndenumerate(grid) if v == 0])
  print("Part 1", paths)
  paths = sum([calc_path(grid, x, y, allowDup=True) for (y, x), v in np.ndenumerate(grid) if v == 0])
  print("Part 2", paths)
