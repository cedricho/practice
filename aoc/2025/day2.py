# https://adventofcode.com/2025/day/2

import sys


def get_ids(s):
  a, b = s.split('-')
  return (a, b)


def read(file):
  with open(file) as f:
    return [get_ids(s) for s in f.readline().split(',')]


def part1(file):
  first_half = lambda x: x[:max(len(x)//2, 1)]
  sum = 0
  for a, b in read(file):
    min_value = int(a)
    max_value = int(b)
    start = int(first_half(a))
    id = int(str(start) * 2)
    while id <= max_value:
      if min_value <= id:
        sum += id
      start += 1
      id = int(str(start) * 2)
  return sum


def part2(file):
  ids = set()
  for a, b in read(file):
    min_value = int(a)
    max_value = int(b)
    start = 1
    repeat = 2
    id = int(str(start) * repeat)
    while id <= max_value or repeat > 2:
      while id < min_value:
        repeat += 1
        id = int(str(start) * repeat)
      while id <= max_value:
        ids.add(id)
        repeat += 1
        id = int(str(start) * repeat)
      start += 1
      repeat = 2
      id = int(str(start) * repeat)
  return sum(ids)


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
