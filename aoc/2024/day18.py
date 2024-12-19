from collections import deque
import numpy as np
import sys

def bfs(grid):
  end = len(grid) - 1
  dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  in_range = lambda x, y: 0 <= x <= end and 0 <= y <= end
  visited = np.zeros_like(grid)
  q = deque()
  q.append((0, 0, 0))
  while q:
    x, y, steps = q.popleft()
    if visited[y, x]: continue
    visited[y, x] = 1
    if x == end and y == end: return steps
    for nx, ny, in [(x+dx, y+dy) for dx, dy in dir]:
      if in_range(nx, ny) and not grid[ny, nx] and not visited[ny, nx]:
        q.append((nx, ny, steps + 1))


def make_grid(size, coords, bytes):
  grid = np.zeros((size, size), dtype=int)
  for x, y in coords[0:bytes]:
    grid[y, x] = 1
  return grid


with open(sys.argv[1]) as f:
  size = int(sys.argv[2])
  part1_bytes = int(sys.argv[3])
  coords = [list(map(int, line.split(','))) for line in f]
  grid = make_grid(size, coords, part1_bytes)
  print("Part 1", bfs(grid))
  for i in range(len(coords)):
    grid = make_grid(size, coords, i)
    if not bfs(grid):
      x, y = coords[i-1]
      print("Part 2", x, y)
      break
