from collections import defaultdict, deque
import itertools
import numpy as np
import sys


directions = [(0, 1, 'D'), (0, -1, 'U'), (1, 0, "R"), (-1, 0, "L")]


def in_range(grid, x, y):
  return 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]


def perimeter(plants, grid):
  p = 0
  for x, y in plants:
    candidates = [(x + dx, y + dy) for dx, dy, _ in directions]
    p += sum(1 for nx, ny in candidates if not in_range(grid, nx, ny) or grid[y, x] != grid[ny, nx])
  return p


def sides(plants, grid):
  segments = defaultdict(list)
  for x, y in plants:
    for nx, ny, dir in [(x + dx, y + dy, dir) for dx, dy, dir in directions]:
      if not in_range(grid, nx, ny) or grid[y, x] != grid[ny, nx]:
        segments[dir].append((x, y))
  counts = 0
  for dir, segs in segments.items():
    counts += 1
    if dir == 'U' or dir == 'D':
      segs.sort(key = lambda e: (e[1], e[0]))
      counts += sum(1 for (x1, y1), (x2, y2) in itertools.pairwise(segs) if y1 != y2 or x1 + 1 != x2)
    else:
      segs.sort(key = lambda e: (e[0], e[1]))
      counts += sum(1 for (x1, y1), (x2, y2) in itertools.pairwise(segs) if x1 != x2 or y1 + 1 != y2)
  return counts


def bfs(grid, visited, x, y):
  plants = []
  q = deque()
  q.append((x, y))
  visited[y, x] = True
  plants.append((x, y))
  while q:
    x, y = q.pop()
    for nx, ny in [(x + dx, y + dy) for dx, dy, _ in directions]:
      if in_range(grid, nx, ny) and grid[y, x] == grid[ny, nx] and not visited[ny, nx]:
        q.append((nx, ny))
        visited[ny, nx] = True
        plants.append((nx, ny))
  return plants


with open(sys.argv[1]) as input:
  grid = np.genfromtxt(input, delimiter=1, dtype=str)
  visited = np.full_like(grid, False, dtype=bool)
  regions = []
  for y, x in np.ndindex(grid.shape):
    if visited[y, x]: continue
    regions.append(bfs(grid, visited, x, y))
    
  print("Part 1", sum(len(r) * perimeter(r, grid) for r in regions))
  print("Part 1", sum(len(r) * sides(r, grid) for r in regions))
