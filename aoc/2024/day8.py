from dataclasses import dataclass
import itertools
import sys


@dataclass(unsafe_hash=True)
class Pos:
  x: int
  y: int


def within_range(pos, width, height):
  return 0 <= pos.x < width and 0 <= pos.y < height


def calc_antinode(pos_list):
  anti = lambda a, b: Pos(2 * a.x - b.x, 2 * a.y - b.y)
  return list(itertools.chain(*[(anti(a, b), anti(b, a)) for a, b in itertools.combinations(pos_list, 2)]))


def calc_antinode_harmonics(pos_list, width, height):
  vec = lambda a, b: Pos(a.x - b.x, a.y - b.y)
  def get_harmonics(a, v):
    res = []
    while True:
      n = Pos(a.x + v.x, a.y + v.y)
      if within_range(n, width, height): res.append(n); a = n
      else: break
    return res

  results = list(pos_list)
  for a, b in itertools.combinations(pos_list, 2):
    v = vec(a, b)
    results.extend(get_harmonics(a, v))
    v = vec(b, a)
    results.extend(get_harmonics(b, v))
  return results


def read_coords(file):
  with open(file) as input:
    grid = [list(line.rstrip()) for line in input]
    return [(c, x, y) for y, row in enumerate(grid) for x, c in enumerate(row) if c != '.'], len(grid[0]), len(grid)


def part1(file):
  coords, width, height = read_coords(file)
  antinode_coords = []
  for _, group in itertools.groupby(sorted(coords), key = lambda c: c[0]):
    antinode_coords.extend(calc_antinode([Pos(x, y) for _, x, y in group]))
  return len(set(p for p in antinode_coords if within_range(p, width, height)))


def part2(file):
  coords, width, height = read_coords(file)
  antinode_coords = []
  for _, group in itertools.groupby(sorted(coords), key = lambda c: c[0]):
    antinode_coords.extend(calc_antinode_harmonics([Pos(x, y) for _, x, y in group], width, height))
  return len(set(antinode_coords))


print("Part 1:", part1(sys.argv[1]))
print("Part 2:", part2(sys.argv[1]))
