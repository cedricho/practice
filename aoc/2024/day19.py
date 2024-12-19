from functools import cache
import sys

towels = []

def possible(design, idx):
  global towels
  if idx == len(design): return True
  for t in towels:
    if design[idx:idx+len(t)] != t: continue
    if possible(design, idx + len(t)): return True
  return False


@cache
def count_possible(design):
  global towels
  if not design: return 1
  counts = 0
  for t in towels:
    if design[0:len(t)] != t: continue
    counts += count_possible(design[len(t):])
  return counts


with open(sys.argv[1]) as f:
  towels = f.readline().rstrip().split(', ')
  f.readline()
  designs = [line.rstrip() for line in f]
  print("Part 1", len([1 for design in designs if possible(design, 0)]))
  print("Part 2", sum([count_possible(design) for design in designs]))
