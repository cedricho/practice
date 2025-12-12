# https://adventofcode.com/2025/day/11

import functools
import sys


def read(file):
  paths = {}
  with open(file) as f:
    for line in f:
      items = line.split()
      paths[items[0][:-1]] = items[1:]
  return paths


def part1(file, src):
  paths = read(file)
  @functools.cache
  def count_paths(node):
    if node == 'out': return 1
    return sum(count_paths(n) for n in paths[node])

  return count_paths(src)


def part2(file, src):
  paths = read(file)
  @functools.cache
  def count_paths(node, dac, fft):
    if node == 'out': return 1 if dac and fft else 0
    return sum(count_paths(n, dac or node=='dac', fft or node=='fft') for n in paths[node])

  return count_paths(src, False, False)


print("Part 1:", part1(sys.argv[1], sys.argv[2]))
print("Part 2:", part2(sys.argv[1], sys.argv[2]))
