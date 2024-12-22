from functools import cache
import itertools as it
import numpy as np
import sys


def is_valid(sx, sy, path, fx, fy):
  dirs = {'<':(-1,0), '>':(1,0), '^':(0,-1), 'v':(0,1)}
  for p in path:
    dx, dy = dirs[p]
    sx += dx; sy += dy
    if sx == fx and sy == fy: return False
  return True


def get_instruction(sx, sy, ex, ey, fx, fy):
  ver_inst = lambda dy: 'v'*dy if dy >= 0 else '^'*-dy
  hor_inst = lambda dx: '>'*dx if dx >= 0 else '<'*-dx
  dx = ex - sx; dy = ey - sy
  paths = set("".join(path) + 'A'
              for path in it.permutations(ver_inst(dy) + hor_inst(dx))
              if is_valid(sx, sy, path, fx, fy))
  return sorted(paths)


def generate_instructions(keypad, fx, fy):
  instructions = {}
  for (sy, sx), s in np.ndenumerate(keypad):
     for (ey, ex), e in np.ndenumerate(keypad):
       if not s or not e: continue
       instructions[(s, e)] = get_instruction(sx, sy, ex, ey, fx, fy) if s != e else ['A']
  return instructions


dir_keypad_instructions = {}


def instructions_for(code, instructions):
  inst_list = [instructions[(p, c)] for p, c in it.pairwise('A' + code) if instructions[(p, c)]]
  return ["".join(s) for s in it.product(*inst_list)]


@cache
def find_cost(p, c, level):
  global dir_keypad_instructions
  if level == 1:
    return len(dir_keypad_instructions[(p, c)][0])
  lowest_cost = 2**63-1
  for code in dir_keypad_instructions[(p, c)]:
    cost = 0
    for np, nc in it.pairwise('A' + code):
      cost += find_cost(np, nc, level - 1)
    if cost < lowest_cost:
      lowest_cost = cost
  return lowest_cost


def find_cost_for_code(code, level):
  return sum(find_cost(p, c, level) for p, c in it.pairwise('A' + code))


def find_all_costs(code_for_numpad_robot, level):
  lowest_costs = []
  for codes in code_for_numpad_robot:
    lowest_costs.append(min(find_cost_for_code(code, level) for code in codes))
  return lowest_costs


with open(sys.argv[1]) as f:
  codes = [line.rstrip() for line in f]
  num_keypad = np.array([['7','8','9'], ['4','5','6'], ['1','2','3'], ['', '0', 'A']])
  num_keypad_instructions = generate_instructions(num_keypad, 0, 3)
  dir_keypad = np.array([['','^','A'], ['<','v','>']])
  dir_keypad_instructions = generate_instructions(dir_keypad, 0, 0)
  code_for_numpad_robot = [instructions_for(code, num_keypad_instructions) for code in codes]

  costs2 = find_all_costs(code_for_numpad_robot, 2)
  print("Part 1", sum(int(code[0:3]) * cost for code, cost in zip(codes, costs2)))
  costs25 = find_all_costs(code_for_numpad_robot, 25)
  print("Part 2", sum(int(code[0:3]) * cost for code, cost in zip(codes, costs25)))
