from collections import defaultdict
from dataclasses import dataclass
import functools
import numpy as np
import re
import sys


width = 101
height = 103


@dataclass
class Robot:
  x: int
  y: int
  vx: int
  vy: int


def readRobots(input):
  matches = [re.match(r'p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)', line) for line in input]
  return [Robot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))) for m in matches]


def calc_pos(r, step):
  return ((r.x + r.vx * step) % width, (r.y + r.vy * step) % height)


def make_grid(pos):
  g = np.zeros((height, width))
  for x, y in pos: g[y, x] += 1
  return g


def print_pos(pos):
  for row in make_grid(pos):
    print("".join(['.' if v == 0 else str(int(v)) for v in row]))


def match_pattern(s, pos, dir, size):
  x, y = pos
  dx, dy = dir
  return sum(1 for i in range(size) if (x + i * dx, y + i * dy) in s) == size


def has_pattern(pos):
  s = set(pos)
  for p in pos:
    if match_pattern(s, p, (1, 1), 3) and match_pattern(s, p, (-1, 1), 3) and match_pattern(s, p, (1, 0), 3): return True
  return False


with open(sys.argv[1]) as input:
  robots = readRobots(input)
  pos = [calc_pos(r, 100) for r in robots]
  hor = width // 2
  ver = height // 2
  quads = defaultdict(lambda: 0)
  for p in pos:
    if p[0] < hor:
      if p[1] < ver: quads[0] += 1
      elif p[1] > ver: quads[1] += 1
    elif p[0] > hor:
      if p[1] < ver: quads[2] += 1
      elif p[1] > ver: quads[3] += 1
  print('Part 1', functools.reduce(lambda x, y: x * y, quads.values()))

  for i in range(100000000):
    pos = [calc_pos(r, i) for r in robots]
    if has_pattern(pos):
      print_pos(pos)
      print("Part 2", i)
      break
