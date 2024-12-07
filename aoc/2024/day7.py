import re
import sys


def eval1(res, a, sum, i):
  if i >= len(a): return False
  plus = sum + a[i]
  mul = sum * a[i]
  if i == len(a) - 1 and (plus == res or mul == res): return True
  return eval1(res, a, plus, i + 1) or eval1(res, a, mul, i + 1)


def eval2(res, a, sum, i):
  if i >= len(a): return False
  plus = sum + a[i]
  mul = sum * a[i]
  cat = int(str(sum) + str(a[i]))
  if i == len(a) - 1 and (plus == res or mul == res or cat == res): return True
  return eval2(res, a, plus, i + 1) or eval2(res, a, mul, i + 1) or eval2(res, a, cat, i + 1)


def get_data(line):
  res, *factors = map(int, re.split(r': | ', line))
  return (res, factors)


def part1(file):
  with open(file) as input:
    data = [get_data(line) for line in input]
    return sum(res for res, a in data if eval1(res, a, a[0], 1))


def part2(file):
  with open(file) as input:
    data = [get_data(line) for line in input]
    return sum(res for res, a in data if eval2(res, a, a[0], 1))


print(part1(sys.argv[1]))
print(part2(sys.argv[1]))
