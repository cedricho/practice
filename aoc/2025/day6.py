# https://adventofcode.com/2025/day/6

import math
import numpy as np
import sys


def sum_results(nums_and_ops):
  total = 0
  for nums, op in nums_and_ops:
    if op == '+':
      total += sum(nums)
    else: # op == '*'
      total += math.prod(nums)
  return total


def read_part1(file):
  with open(file) as input:
    lines = [line.strip() for line in input]
    line_items = [line.split() for line in lines]
    result = []
    for i in range(len(line_items[0])):
      op = line_items[-1][i]
      nums = [int(line_item[i]) for line_item in line_items[:-1]]
      result.append((nums, op))
    return result


def read_part2(file):
  data = np.genfromtxt(file, dtype=str, delimiter=1)
  result = []
  nums = []
  op = ''
  for i in range(data.shape[1]):
    if data[-1, i] in ('+', '*'):
      if nums:
        result.append((nums, op))
        nums = []
      op = data[-1, i]
    if n := ''.join(data[:-1, i]).strip():
      nums.append(int(n))
  if nums:
    result.append((nums, op))
  return result


print("Part 1:", sum_results(read_part1(sys.argv[1])))
print("Part 2:", sum_results(read_part2(sys.argv[1])))