import itertools
import re
import sys

def part1(file):
  with open(file) as input:
    regex = re.compile(r"mul\((\d+),(\d+)\)")
    nums = itertools.chain(*[regex.findall(line) for line in input.readlines()])
    return sum(int(a) * int(b) for a, b in nums)

def part2(file):
  with open(file) as input:
    regex = re.compile(r"(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)")
    entries = itertools.chain(*[regex.findall(line) for line in input.readlines()])
    sum = 0; active = True
    for do, dont, a, b in entries:
      if do or dont: active = bool(do)
      elif active: sum += int(a) * int(b)
    return sum

print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))