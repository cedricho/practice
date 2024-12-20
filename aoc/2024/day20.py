import numpy as np
import sys


def calc(grid):
  costs = np.full(grid.shape, -1, dtype=int)
  sx, sy = next((x, y) for (y, x), v in np.ndenumerate(grid) if v == 'S')
  in_range = lambda x, y: 0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]
  car = sx, sy
  cost = 0
  while True:
    x, y = car
    costs[y, x] = cost
    if grid[y, x] == 'E': break
    for nx, ny in [(x+dx, y+dy) for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]]:
      if in_range(nx, ny) and (grid[ny, nx] == '.' or grid[ny, nx] == 'E') and costs[ny, nx] == -1:
        car = (nx, ny); cost += 1; break
  return costs


def count_shortcuts(costs, threshold):
  in_range = lambda x, y: 0 <= x < costs.shape[1] and 0 <= y < costs.shape[0]
  counts = 0
  for (y, x), cost in np.ndenumerate(costs):
    if cost == -1: continue
    for nx, ny in [(x+dx, y+dy) for dx, dy in [(0,2),(2,0),(0,-2),(-2,0)]]:
      if in_range(nx, ny) and (costs[ny, nx] - (cost + 2)) >= threshold:
        counts += 1
  return counts


def count_crazy_shortcuts(costs, threshold):
  in_range = lambda x, y: 0 <= x < costs.shape[1] and 0 <= y < costs.shape[0]
  counts = 0
  cheat_costs = [(x, y, abs(x) + abs(y)) for x in range(-20,21) for y in range(-20,21) if 1 < abs(x) + abs(y) <= 20]
  for (y, x), cost in np.ndenumerate(costs):
    if cost == -1: continue
    for nx, ny, cheat_cost in [(x+dx, y+dy, cheat_cost) for dx, dy, cheat_cost in cheat_costs]:
      if in_range(nx, ny) and (costs[ny, nx] - (cost + cheat_cost)) >= threshold:
        counts += 1
  return counts


with open(sys.argv[1]) as f:
  threshold = int(sys.argv[2])
  grid = np.genfromtxt(f, dtype=str, delimiter=1, comments=None)
  costs = calc(grid)
  print("Part 1", count_shortcuts(costs, threshold))
  print("Part 2", count_crazy_shortcuts(costs, threshold))
