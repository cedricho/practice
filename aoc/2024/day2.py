import itertools
import sys


def is_safe(report):
  diffs = [i - j for i, j in itertools.pairwise(report)]
  return all(0 < d < 4 for d in diffs) or all(-4 < d < 0 for d in diffs)


def part1(file):
  with open(file) as input:
    reports = [list(map(int, line.split())) for line in input.readlines()]
    return sum([1 if is_safe(r) else 0 for r in reports])


def is_dampener_safe(report):
  return any(is_safe(report[0:i] + report[i+1:]) for i, _ in enumerate(report))


def part2(file):
  with open(file) as input:
    reports = [list(map(int, line.split())) for line in input.readlines()]
    return sum([1 if is_dampener_safe(r) else 0 for r in reports])


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
