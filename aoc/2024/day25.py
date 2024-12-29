import itertools as it
import numpy as np
import sys


def get_heights(lines):
  h = np.zeros(5)
  for line in lines:
    h += np.array([1 if c == '#' else 0 for c in line])
  return h


def read(lines):
  locks = []
  keys = []
  for i in range(0, len(lines), 8):
    if all(c == '#' for c in lines[i]):
      locks.append(get_heights(lines[i+1:i+6]))
    else:
      keys.append(get_heights(lines[i+1:i+6]))
  return locks, keys


with open(sys.argv[1]) as f:
  locks, keys = read([line.rstrip() for line in f])
  fits = 0
  for lock, key in it.product(locks, keys):
    if all(sum <= 5 for sum in lock + key): fits += 1
  print(fits)
