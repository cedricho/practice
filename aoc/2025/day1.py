# https://adventofcode.com/2025/day/1

import sys


def read(file):
  get_value = lambda s: int(s[1:]) if s[0] == 'R' else -int(s[1:])
  with open(file) as input:
    return [get_value(line.strip()) for line in input]


def part1(file):
  count = 0
  dial = 50
  for step in read(file):
    dial = (dial + step) % 100
    if dial == 0:
      count += 1
  return count


def part2(file):
  count = 0
  dial = 50
  for step in read(file):
    t = dial + step
    new_dial = t % 100
    offset = 0
    if step < 0:
      if dial == 0:
        offset = -1
      elif new_dial == 0:
        offset = 1
    count_delta = abs(t // 100) + offset
    count += count_delta
    dial = new_dial
  return count

print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
