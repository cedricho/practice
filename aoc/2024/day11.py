import functools
import sys


@functools.cache
def count_rocks(i, step):
  if step == 0:
    return 1
  if i == 0:
    return count_rocks(1, step - 1)
  s = str(i); l = len(s)
  if l % 2 == 0:
    h = l // 2
    return count_rocks(int(s[0:h]), step - 1) + count_rocks(int(s[h:]), step - 1)
  else:
    return count_rocks(i * 2024, step - 1)


with open(sys.argv[1]) as input:
  seq = list(map(int, input.readline().split()))
  print("part 1", sum(count_rocks(i, 25) for i in seq))
  print("part 2", sum(count_rocks(i, 75) for i in seq))
