import collections
import sys


def read(file):
  with open(file) as input:
    return zip(*[map(int, line.split()) for line in input])


def part1(file):
  a, b = read(file)
  diffs = [abs(a - b) for a, b in zip(sorted(a), sorted(b))]
  return sum(diffs)


def part2(file):
  a, b = read(file)
  c = collections.Counter(b)
  return sum(i * c[i] for i in a)


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
