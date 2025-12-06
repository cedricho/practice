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
    ops = lines[-1].split()
    lines = lines[:-1]
    nums = np.zeros((len(lines), len(ops)), dtype=int)
    for i in range(len(lines)):
      nums[i] = [int(v) for v in lines[i].split()]
    result = []
    for i in range(len(ops)):
      result.append((nums[:, i], ops[i]))
    return result


def read_part2(file):
  with open(file) as input:
    lines = [line.rstrip('\n') for line in input]
    ops = lines[-1].split()
    lines = lines[:-1]
    raw = np.empty((len(lines), len(lines[0])), dtype=str)
    for i in range(len(lines)):
      raw[i] = list(lines[i])

    result = []
    ops_idx = 0
    nums = []
    for i in range(raw.shape[1]):
      if n := ''.join(raw[:, i]).strip():
        nums.append(int(n))
      else:
        result.append((nums, ops[ops_idx]))
        ops_idx += 1
        nums = []
    result.append((nums, ops[ops_idx]))
    return result


print("Part 1:", sum_results(read_part1(sys.argv[1])))
print("Part 2:", sum_results(read_part2(sys.argv[1])))