from __future__ import annotations
from dataclasses import dataclass
import heapq
import numpy as np
import sys

step = {"E": (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}
dirs = "ESWN"


@dataclass(eq=True, unsafe_hash=True)
class Item:
  x: int
  y: int
  d: str
  c: int
  prev: Item
  def __lt__(self, other): return self.c < other.c


def find(grid, t):
  for (y, x), v in np.ndenumerate(grid):
    if v == t: return (x, y)


def count_tiles(traces):
  tiles = set()
  for it in traces:
    while it:
      tiles.add((it.x, it.y))
      it = it.prev
  return len(tiles)


def go(grid):
  sx, sy = find(grid, 'S')
  ex, ey = find(grid, 'E')

  costs = np.full((*grid.shape, 4), 2**63-1, dtype=int)
  def visit(x, y, d, cost):
    if costs[y, x, dirs.index(d)] > cost: costs[y, x, dirs.index(d)] = cost
  is_visited = lambda x, y, d, cost: cost > costs[y, x, dirs.index(d)]

  best_cost = 2**63-1
  backtraces = []
  pq = []
  heapq.heappush(pq, Item(sx, sy, 'E', 0, None))
  while pq:
    it = heapq.heappop(pq)
    if is_visited(it.x, it.y, it.d, it.c): continue
    if (ex, ey) == (it.x, it.y):
      if best_cost >= it.c:
        best_cost = it.c
        backtraces.append(it)
    visit(it.x, it.y, it.d, it.c)
    nx, ny = it.x + step[it.d][0], it.y + step[it.d][1]
    if grid[ny, nx] == '.' or grid[ny, nx] == 'E': heapq.heappush(pq, Item(nx, ny, it.d, it.c+1, it))
    dleft = dirs[(dirs.index(it.d) + 3) % 4]
    heapq.heappush(pq, Item(it.x, it.y, dleft, it.c+1000, it))
    dright = dirs[(dirs.index(it.d) + 1) % 4]
    heapq.heappush(pq, Item(it.x, it.y, dright, it.c+1000, it))

  return best_cost, count_tiles(backtraces)


with open(sys.argv[1]) as input:
  grid = np.genfromtxt(input, delimiter=1, dtype=str, comments='/')
  p1, p2 = go(grid)
  print("Part 1", p1)
  print("Part 2", p2)
 