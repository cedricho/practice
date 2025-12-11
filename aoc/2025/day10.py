# https://adventofcode.com/2025/day/10

from dataclasses import dataclass
import sys
import pulp


@dataclass
class Machine:
  lights: str
  buttons: list[set[int]]
  joltages: tuple[int]

  @classmethod
  def parse(cls, line: str):
    parse_numbers = lambda line: [int(s) for s in line[1:-1].split(',')]
    items = line.split()
    lights = items[0][1:-1]
    buttons = [parse_numbers(item) for item in items[1:-1]]
    joltages = tuple(parse_numbers(items[-1]))
    return cls(lights, buttons, joltages)


def read(file):
  with open(file) as f:
    return [Machine.parse(line.strip()) for line in f]


def press(config, button_wiring):
  new_config = []
  for i, v in enumerate(config):
    flip = i in button_wiring
    ch = v if not flip else '.' if v == '#' else '#'
    new_config.append(ch)
  return ''.join(new_config)


def solve1(machine):
  all_off = '.' * len(machine.lights)
  checked = set(all_off)
  queue = [(all_off, 0)]
  while queue:
    config, count = queue.pop(0)
    for button in machine.buttons:
      new_config = press(config, button)
      if new_config == machine.lights:
        return count + 1
      if new_config in checked:
        continue
      else:
        checked.add(new_config)
        queue.append((new_config, count + 1))


def part1(file):
  machines = read(file)
  return sum(solve1(m) for m in machines)


def press_handle(joltages, button_wiring):
  new_joltages = []
  for i, v in enumerate(joltages):
    new_joltages.append(v - 1 if i in button_wiring else v)
  if any(j < 0 for j in new_joltages):
    return None
  return tuple(new_joltages)


def build_objective(vars):
  v = vars[0]
  for var in vars[1:]:
    v = v + var
  return v, "Objective function"


def build_equations(eq, joltage, vars, buttons):
  eq_vars = [var for var in vars if eq in buttons[int(var.name[1:])]]
  v = eq_vars[0]
  for var in eq_vars[1:]:
    v = v + var
  return v == joltage, "Equation " + str(eq)


def solve2(machine):
  prob = pulp.LpProblem("solve_for_positive_integers", pulp.LpMinimize)
  vars = [pulp.LpVariable('x'+str(i), lowBound=0, cat='Integer') for i in range(len(machine.buttons))]
  prob += build_objective(vars)
  for eq, joltage in enumerate(machine.joltages):
    prob += build_equations(eq, joltage, vars, machine.buttons)
  prob.solve()
  if pulp.LpStatus[prob.status] == 'Optimal':
    return sum(int(v.varValue) for v in prob.variables())
  else:
    print("No solution!")
    sys.exit(1)


def part2(file):
  machines = read(file)
  return sum(solve2(m) for m in machines)


p1 = part1(sys.argv[1])
p2 = part2(sys.argv[1])
print("Part 1:", p1)
print("Part 2:", p2)
