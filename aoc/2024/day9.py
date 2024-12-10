from dataclasses import dataclass
import sys


def read(file):
  with open(file) as input:
    return map(int, list(input.readline().rstrip()))


def expand(compact):
  expanded = []
  is_file = True
  file_id = 0
  for size in compact:
    if is_file: expanded.extend([file_id] * size); file_id += 1
    else: expanded.extend([-1] * size)
    is_file = not is_file
  return expanded


def defrag(disk):
  s = 0; e = len(disk) - 1
  while s < e:
    if disk[s] != -1: s += 1; continue
    if disk[e] == -1: e -= 1; continue
    disk[s] = disk[e]; disk[e] = -1
  return disk


def part1(file):
  compact = read(file)
  expanded = expand(compact)
  defraged = defrag(expanded)
  return sum(i * v for i, v in enumerate(defraged) if v >= 0)


def find_file_block(disk, id):
  return (disk.index(id), disk.count(id))


def find_free_block(disk, l, end):
  for s in range(end):
    if disk[s] != -1: continue
    if all(d == -1 for d in disk[s:s+l]): return s
  return -1


def defrag2(disk):
  file_id = max(disk)
  for id in range(file_id, -1, -1):
    fs, fl = find_file_block(disk, id)
    if (s := find_free_block(disk, fl, fs)) < 0: continue
    disk[s:s+fl] = [id] * fl
    disk[fs:fs+fl] = [-1] * fl
  return disk


def part2(file):
  compact = read(file)
  expanded = expand(compact)
  defraged = defrag2(expanded)
  return sum(i * v for i, v in enumerate(defraged) if v >= 0)


print("Part 1", part1(sys.argv[1]))
print("Part 2", part2(sys.argv[1]))
