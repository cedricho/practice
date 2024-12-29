import re
import sys

def read_input(lines):
  idx = next(i for i, line in enumerate(lines) if not line)
  init_values = {}
  for line in lines[0:idx]:
    m = re.match(r'(.+): (\d)', line)
    init_values[m.group(1)] = int(m.group(2))
  gates = {}
  z_wires = []
  for line in lines[idx+1:]:
    m = re.match(r'(.+) (.+) (.+) -> (.+)', line)
    i1, op, i2, out = m.groups()
    if out.startswith('z'): z_wires.append(out)
    gates[out] = (op, i1, i2)
  return init_values, gates, sorted(z_wires)


def gate(op, v1, v2):
  if op == 'AND': return v1 & v2
  if op == 'OR': return v1 | v2
  if op == 'XOR': return v1 ^ v2


def calc(values, gates, wire):
  if wire in values: return values[wire]
  op, i1, i2 = gates[wire]
  v1 = calc(values, gates, i1)
  v2 = calc(values, gates, i2)
  out = gate(op, v1, v2)
  values[wire] = out
  return out


def both_equal(i1, i2, s1, s2):
  return (i1 == s1 and i2 == s2) or (i1 == s2 and i2 == s1)


def wire(name, pos):
  return name + '{:02d}'.format(pos)


def check_adder(gates, pos):
  A = B = D = Sum = Carry = None
  x, y = wire('x', pos), wire('y', pos)
  for out, gate in gates.items():
    op, i1, i2 = gate
    direct_input = both_equal(i1, i2, x, y)
    if direct_input and op == 'XOR': A = out
    if direct_input and op == 'AND': B = out
  for out, gate in gates.items():
    op, i1, i2 = gate
    if op == 'AND' and (i1 == A or i2 == A): D = out
    if op == 'XOR' and (i1 == A or i2 == A): Sum = out
    if op == 'OR' and (i1 == B or i2 == B): Carry = out
  print(x, y, '-', A, B, D, Sum, Carry) # and manually find the pairs


with open(sys.argv[1]) as f:
  init_values, gates, z_wires = read_input([line.rstrip() for line in f])
  final_value = 0
  for z in z_wires:
    pos = int(z[1:])
    v = calc(dict(init_values), gates, z)
    final_value += v << pos
  print('Part 1', final_value)

  wire_num = {}
  for z in z_wires:
    pos = int(z[1:])
    check_adder(gates, pos)