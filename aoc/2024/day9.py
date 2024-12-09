from dataclasses import dataclass
import itertools
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
  while True:
    while s < e and disk[s] != -1: s += 1
    while s < e and disk[e] == -1: e -= 1
    if s >= e: break
    disk[s] = disk[e]; disk[e] = -1
  return disk


@dataclass
class Block:
  file_id: int
  start: int
  size: int


def get_block_list(compact):
  blocks = []
  is_file = True
  start = 0
  file_id = 0
  for size in compact:
    if is_file: blocks.append(Block(file_id, start, size)); file_id += 1; start += size
    else: blocks.append(Block(-1, start, size)); start += size
    is_file = not is_file
  return blocks


def defrag_blocks(blocks):
  e = len(blocks) - 1
  while True:
    while 0 <= e and blocks[e].file_id == -1: e -= 1
    if 0 > e: break
    s = 0
    while s < e and (blocks[s].file_id != -1 or blocks[s].size < blocks[e].size): s += 1
    if s >= e: e -=1; continue
    gap = blocks[s].size - blocks[e].size
    gap_start = blocks[s].start + blocks[e].size
    blocks[s].file_id = blocks[e].file_id
    blocks[s].size = blocks[e].size
    blocks[e].file_id = -1
    if gap > 0:
      blocks = blocks[0:s+1] + [Block(-1, gap_start, gap)] + blocks[s+1:]
      e += 1
  return blocks


def expand_blocks(defraged):
  expanded = []
  for b in defraged:
    expanded.extend([b.file_id]*b.size)
  return expanded


def part1(file):
  compact = read(file)
  expanded = expand(compact)
  defraged = defrag(expanded)
  return sum(i * v for i, v in enumerate(defraged) if v >= 0)


def part2(file):
  compact = read(file)
  blocks = get_block_list(compact)
  defraged = defrag_blocks(blocks)
  expanded = list(itertools.chain(*[[b.file_id]*b.size for b in defraged]))
  return sum(i * v for i, v in enumerate(expanded) if v >= 0)


print("Part 1", part1(sys.argv[1]))
print("Part 2", part2(sys.argv[1]))
