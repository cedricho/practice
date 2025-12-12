# https://adventofcode.com/2025/day/12#part2

import sys


def read(file):
  cases = []
  with open(file) as f:
    for line in f:
      items = line.split()
      if len(items) < 2: continue
      area = tuple(map(int, items[0][:-1].split('x')))
      num_shapes = sum(map(int, items[1:]))
      cases.append((area, num_shapes))
  return cases


cases = read(sys.argv[1])
print(sum(True for c in cases if c[0][0]*c[0][1] >= c[1] * 9))
