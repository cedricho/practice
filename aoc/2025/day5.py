# https://adventofcode.com/2025/day/5

import sys


def read(file):
  read_range = True
  id_ranges = []
  ids = []
  with open(file) as input:
    for line in input:
      line = line.strip()
      if line == "":
        read_range = False
        continue
      if read_range:
        parts = line.split("-")
        id_ranges.append((int(parts[0]), int(parts[1])))
      else:
        ids.append(int(line))
  return id_ranges, ids


def part1(file):
  id_ranges, ids = read(file)
  fresh = 0
  in_range = lambda id, r: r[0] <= id <= r[1]
  for id in ids:
    if any(in_range(id, r) for r in id_ranges):
      fresh += 1
  return fresh


def part2(file):
  id_ranges, _ = read(file)
  id_ranges.sort(key = lambda r: r[0])
  merged_ranges = []
  for r in id_ranges:
    if not merged_ranges or merged_ranges[-1][1] < r[0] - 1:
      merged_ranges.append(r)
    else:
      merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]))
  return sum(r[1] - r[0] + 1 for r in merged_ranges)


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
