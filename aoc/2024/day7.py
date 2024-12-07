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


def part1(file):
  with open(file) as input:
    lines = [line.split(':') for line in input]
    lines = [(int(res), list(map(int, a.split()))) for res, a in lines]
    return sum(res for res, a in lines if eval1(res, a, a[0], 1))


def part2(file):
  with open(file) as input:
    lines = [line.split(':') for line in input]
    lines = [(int(res), list(map(int, a.split()))) for res, a in lines]
    return sum(res for res, a in lines if eval2(res, a, a[0], 1))


print(part1(sys.argv[1]))
print(part2(sys.argv[1]))
