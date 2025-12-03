# https://adventofcode.com/2025/day/3

import sys


def read_input(file):
  with open(file, 'r') as input:
    return [line.strip() for line in input]


def part1(file):
  banks = read_input(file)
  sum = 0
  for bank in banks:
    digit1 = max(bank[:-1])
    idx = bank.index(digit1)
    digit2 = max(bank[idx+1:])
    sum += int(digit1 + digit2)
  return sum


def part2(file):
  banks = read_input(file)
  sum = 0
  for bank in banks:
    digits = []
    start, end = 0, -11
    while end < 0:
      digits.append(max(bank[start:end]))
      start = bank.index(digits[-1], start) + 1
      end += 1
    digits.append(max(bank[start:]))
    sum += int(''.join(digits))
  return sum


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))