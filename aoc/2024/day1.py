import collections
import sys

# Part 1
def part1(file):
  with open(file) as input:
    a, b = zip(*[line.split() for line in input.readlines()])
    diffs = [abs(a - b) for a, b in zip(sorted(map(int, a)), sorted(map(int, b)))]
    return sum(diffs)

# Part 2
def part2(file):
  with open(file) as input:
    a, b = zip(*[line.split() for line in input.readlines()])
    c = collections.Counter(map(int, b))
    return sum(i * c[i] for i in map(int, a))

file = sys.argv[1]
print("Part 1:", part1(file))
print("Part 2:", part2(file))
