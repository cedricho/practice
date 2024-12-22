from collections import defaultdict
import sys

def evolve(num):
  MASK_24 = (1 << 24) - 1
  num = ((num << 6) ^ num) & MASK_24
  num = ((num >> 5) ^ num) & MASK_24
  return ((num << 11) ^ num) & MASK_24


def generator(num):
  while True: yield (num:= evolve(num))


def next_i(g, i):
   for _ in range(i-1): next(g)
   return next(g)


def gen_diffs(num):
  d1 = d2 = d3 = d4 = None
  while True:
    num = evolve(prev := num)
    d1, d2, d3, d4 = d2, d3, d4, (num % 10 - prev % 10)
    yield num % 10, (d1, d2, d3, d4)


def add_monkey(gen, seq_price_total):
  seen_seq = set()
  for _ in range(2000):
    price, seq = next(gen)
    if seq[0] == None or seq in seen_seq: continue
    seq_price_total[seq] += price
    seen_seq.add(seq)


with open(sys.argv[1]) as f:
  seeds = [int(line) for line in f]
  print("Part 1", sum(next_i(generator(s), 2000) for s in seeds))
  seq_price_total = defaultdict(int)
  for g in [gen_diffs(s) for s in seeds]:
    add_monkey(g, seq_price_total)
  print("Part 2", max(seq_price_total.values()))
