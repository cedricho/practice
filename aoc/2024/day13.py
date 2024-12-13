from dataclasses import dataclass
import functools
import re
import sys


@dataclass(unsafe_hash=True)
class Button:
  x: int
  y: int
  cost: int


@dataclass(unsafe_hash=True)
class Machine:
  a: Button
  b: Button
  px: int
  py: int


def read_machines(lines, offset=0):
  machines = []
  for i in range(0, len(lines), 4):
    x, y = re.search(r'X\+(\d+), Y\+(\d+)', lines[i]).group(1, 2)
    a = Button(int(x), int(y), 3)
    x, y = re.search(r'X\+(\d+), Y\+(\d+)', lines[i+1]).group(1, 2)
    b = Button(int(x), int(y), 1)
    x, y = re.search(r'X=(\d+), Y=(\d+)', lines[i+2]).group(1, 2)
    machines.append(Machine(a, b, int(x) + offset, int(y) + offset))
  return machines


@functools.cache
def calc_cost(m, cx = 0, cy = 0, ai = 0, bi = 0, cost = 0):
  if m.px == cx and m.py == cy: return cost
  if m.px < cx or m.py < cy or ai > 100 or bi > 100: return -1
  costA = calc_cost(m, cx + m.a.x, cy + m.a.y, ai + 1, bi, cost + m.a.cost)
  costB = calc_cost(m, cx + m.b.x, cy + m.b.y, ai, bi + 1, cost + m.b.cost)
  if costA == -1: return costB
  if costB == -1: return costA
  return min(costA, costB)


def efficient_calc_cost(m):
  # ax * ai + bx * bi = px
  # ay * ai + by * bi = py
  # (px - bx * bi) / ax = (py - by * bi) / ay
  # ay * px - ay * bx * bi = ax * py - ax * by * bi
  # ay * px - ax * py = (ay * bx - ax * by) * bi
  # bi = (ay * px - ax * py) / (ay * bx - ax * by)
  c1 = m.a.y * m.px - m.a.x * m.py
  c2 = m.a.y * m.b.x - m.a.x * m.b.y
  if c1 % c2 != 0: return 0
  bi = c1 // c2
  ai = (m.px - m.b.x * bi) // m.a.x
  return ai * 3 + bi


with open(sys.argv[1]) as input:
  lines = input.readlines()
  machines = read_machines(lines)
  print("Part 1:", sum(max(calc_cost(m), 0) for m in machines))

  machines = read_machines(lines, offset=10000000000000)
  print("Part 2:", sum(efficient_calc_cost(m) for m in machines))
