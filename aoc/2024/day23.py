from collections import defaultdict
import itertools as it
import sys

with open(sys.argv[1]) as f:
  pairs = [line.rstrip().split('-') for line in f]
  pc_link = defaultdict(set)
  for a, b in pairs:
    pc_link[a].add(b)
    pc_link[b].add(a)
  groups = set()  
  for k in pc_link:
    if not k.startswith('t'): continue
    for a, b in it.combinations(pc_link[k], 2):
      if a in pc_link[b]:
        groups.add(tuple(sorted([k, a, b])))
  print("Part 1", len(groups))

  largest = 0
  largest_set = {}
  for k in pc_link:
    potential = {k}
    for c in pc_link[k]:
      if c in potential or not potential.issubset(pc_link[c]): continue
      potential.add(c)
    if len(potential) > largest:
      largest = len(potential)
      largest_set = potential
  print('Part 2', ",".join(sorted(list(largest_set))))
