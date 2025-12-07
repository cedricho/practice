# https://adventofcode.com/2025/day/7

import functools
import numpy as np
import sys


def part1(file):
  data = np.genfromtxt(file, dtype=str, delimiter=1)
  count = 0
  beams = set()
  beams.add(np.where(data[0, :] == 'S')[0][0].item())
  for row in range(1, data.shape[0]):
    new_beams = set()
    for beam in beams:
      if data[row, beam] == '.':
        new_beams.add(beam)
      else: # data[row, beam] == '^'
        count += 1
        if beam -1 >= 0:
          new_beams.add(beam-1)
        if beam +1 < data.shape[1]:
          new_beams.add(beam+1)
    beams = new_beams
  return count


def part2(file):
  data = np.genfromtxt(file, dtype=str, delimiter=1)

  @functools.cache
  def count_paths(row, col):
    if row == data.shape[0]:
      return 1
    if data[row, col] == '.':
      return count_paths(row + 1, col)
    else: # data[row, col] == '^'
      total = 0
      if col - 1 >= 0:
        total += count_paths(row + 1, col - 1)
      if col + 1 < data.shape[1]:
        total += count_paths(row + 1, col + 1)
      return total

  return count_paths(1, col = np.where(data[0, :] == 'S')[0][0].item())


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
