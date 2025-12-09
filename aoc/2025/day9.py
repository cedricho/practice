# https://adventofcode.com/2025/day/9

import itertools as it
# import matplotlib.pyplot as plt
import sys


def read(file):
  to_coord = lambda line: tuple(int(x) for x in line.split(','))
  with open(file) as f:
    return [to_coord(line) for line in f]


def calc_area(p1, p2):
  return (abs(p1[0]-p2[0])+1) * (abs(p1[1]-p2[1])+1)


def part1(file):
  pts = read(file)
  return max(calc_area(p1, p2) for p1, p2 in it.combinations(pts, 2))


def overlap(p1, p2, pts):
  (x1, y1), (x2, y2) = p1, p2
  if x1 > x2: x1, x2 = x2, x1
  if y1 > y2: y1, y2 = y2, y1
  # Check points in rect
  if any(x1 < x < x2 and y1 < y < y2 for x, y in pts):
    return True
  # Check line cross
  for (ex1, ey1), (ex2, ey2) in it.pairwise(pts + [pts[0]]):
    if ex1 == ex2:
      if ex1 <= x1 or ex1 >= x2: continue
      if ey1 > ey2: ey1, ey2 = ey2, ey1
      if ey1 < y2 and y1 < ey2: return True
    else: # ey1 == ey2
      if ey1 <= y1 or ey1 >= y2: continue
      if ex1 > ex2: ex1, ex2 = ex2, ex1
      if ex1 < x2 and x1 < ex2: return True


def part2(file):
  pts = read(file)
  # This does not work for a general solution. It just happened to work for this input.
  return max(calc_area(p1, p2) for p1, p2 in it.combinations(pts, 2) if not overlap(p1, p2, pts))


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))


# Look at the shape:
# pts = read(sys.argv[1])
# xs, ys = zip(*pts)
# plt.plot(xs, ys)
# plt.scatter(xs, ys, color='red')
# plt.show()
