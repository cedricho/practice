import sys
import re

class Machine:
  def __init__(self, registers, program):
    self.A, self.B, self.C = registers
    self.program = program
    self.pi = 0
    self.outputs = []
    self.ops = {0: self.adv, 1: self.bxl, 2: self.bst, 3: self.jnz, 4: self.bxc, 5: self.out, 6: self.bdv, 7: self.cdv}
  
  def combo(self, v):
    if 0 <= v <= 3: return v
    if v == 4: return self.A
    if v == 5: return self.B
    if v == 6: return self.C

  def adv(self, v): self.A = self.A // 2**self.combo(v)
  def bxl(self, v): self.B = self.B ^ v
  def bst(self, v): self.B = self.combo(v) % 8
  def jnz(self, v):
    if self.A: self.pi = v - 2
  def bxc(self, _): self.B = self.B ^ self.C
  def out(self, v): self.outputs.append(self.combo(v) % 8)
  def bdv(self, v): self.B = self.A // 2**self.combo(v)
  def cdv(self, v): self.C = self.A // 2**self.combo(v)

  def run(self):
    while self.pi < len(self.program):
      self.ops[self.program[self.pi]](self.program[self.pi+1])
      self.pi += 2


def opt_program(A):
  outputs = []
  while A > 0:
    B = (A % 8) ^ 7
    C = A // (2**B)
    B = B ^ 7
    A = A // 8
    outputs.append((B ^ C) % 8)
  return outputs


def try_val(lookups, program, i, cur):
  if i >= len(program): return cur
  target = program[i]
  for v in lookups[target]:
    v_hi3, v_lo7 = v>>7, v%128
    cur_hi7 = (cur>>(i*3))%128
    if cur_hi7 != v_lo7: continue
    try_cur = (v_hi3<<(i*3+7)) + cur
    if res := try_val(lookups, program, i+1, try_cur): return res
  return None


def calcA(program):
  lookups = [[] for _ in range(8)]
  for i in range(1, 1024):
    res = opt_program(i)
    lookups[res[0]].append(i)
  for v in lookups[program[0]]:
    if res := try_val(lookups, program, 1, v): return res


with open(sys.argv[1]) as input:
  lines = input.readlines()
  registers = [int(re.search(r'(\d+)', lines[i]).group(1)) for i in range(3)]
  program = list(map(int, re.search(r': (.+)', lines[4]).group(1).split(',')))
  machine = Machine(registers, program)
  machine.run()
  print("Part 1", ",".join(map(str, machine.outputs)))
  print("Part 2", calcA(program))
