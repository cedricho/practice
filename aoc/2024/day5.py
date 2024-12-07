from collections import defaultdict
import itertools
import sys


def readData(file):
  with open(file) as input:
    rules = defaultdict(set)
    updates = []
    for line in input:
      if '|' in line:
        a, b = line.rstrip().split('|')
        rules[a].add(b)
      elif ',' in line:
        updates.append(line.rstrip().split(','))
    return rules, updates


def obey(update, rules):
  for a, b in itertools.combinations(update, 2):
    if b not in rules[a]: return False
  return True


def fix_order(update, rules):
  visited = set()
  order = []

  def topological_sort(rules, node):
    visited.add(node)
    for neighbor in rules[node]:
      if neighbor not in update: continue
      if neighbor not in visited:
        topological_sort(rules, neighbor)
    order.append(node)

  for node in update:
    if node not in visited:
      topological_sort(rules, node)
  return list(reversed(order))


def part1(file):
  rules, updates = readData(file)
  correct_updates = [u for u in updates if obey(u, rules)]
  return sum(int(u[len(u)//2]) for u in correct_updates)


def part2(file):
  rules, updates = readData(file)
  incorrect_updates = [u for u in updates if not obey(u, rules)]
  fixed_updates = [fix_order(u, rules) for u in incorrect_updates]
  return sum(int(u[len(u)//2]) for u in fixed_updates)


print("Part 1", part1(sys.argv[1]))
print("Part 2", part2(sys.argv[1]))
