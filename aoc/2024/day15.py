import itertools
import sys


inst = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}


def print_grid(g):
  for row in g:
    print("".join(row))


def find_robot(grid):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == '@': return x, y
  return None, None


def read(lines):
  lines = [line.rstrip() for line in lines]
  idx = lines.index('')
  grid = [list(line) for line in lines[0:idx]]
  instructions = list(itertools.chain(*lines[idx+1:]))
  return grid, instructions


def move(grid, x, y, dx, dy, obj):
  gv = grid[y][x]
  if gv == '#': return False
  if gv == '.': grid[y][x] = obj; return True
  if gv == 'O':
    if move(grid, x+dx, y+dy, dx, dy, gv):
      grid[y][x] = obj; return True
    else:
      return False
  else: raise ValueError('error')


def large_grid(grid):
  def large(v):
    if v == '#': return ['#', '#']
    if v == 'O': return ['[', ']']
    if v == '.': return ['.', '.']
    if v == '@': return ['@', '.']

  large_grid = []
  for row in grid:
    large_grid.append(list(itertools.chain(*[large(v) for v in row])))
  return large_grid


def can_move_vert(grid, x, y, dy):
  gv = grid[y][x]
  if gv == '.': return True
  if gv == '#': return False
  if gv == '[': return can_move_vert(grid, x, y+dy, dy) and can_move_vert(grid, x+1, y+dy, dy)
  if gv == ']': return can_move_vert(grid, x, y+dy, dy) and can_move_vert(grid, x-1, y+dy, dy)
  else: raise ValueError("error")


def move_vert(grid, x, y, dy, obj):
  gv = grid[y][x]
  if gv == '.':
    grid[y][x] = obj
  elif gv == '[':
    move_vert(grid, x, y+dy, dy, '['); move_vert(grid, x+1, y+dy, dy, ']')
    grid[y][x] = obj; grid[y][x+1] = '.'
  elif gv == ']':
    move_vert(grid, x, y+dy, dy, ']'); move_vert(grid, x-1, y+dy, dy, '[')
    grid[y][x] = obj; grid[y][x-1] = '.'
  else:
    raise ValueError("error")


def move_horz(grid, x, y, dx, obj):
  gv = grid[y][x]
  if gv == '#': return False
  if gv == '.': grid[y][x] = obj; return True
  if gv == '[' or gv == ']':
    if move_horz(grid, x+dx, y, dx, gv):
      grid[y][x] = obj
      return True
    else:
      return False
  else:
    raise ValueError("error")


with open(sys.argv[1]) as input:
  lines = input.readlines()
  grid, instructions = read(lines)
  rx, ry = find_robot(grid)
  for i in instructions:
    dx, dy = inst[i]
    if move(grid, rx+dx, ry+dy, dx, dy, '@'):
      grid[ry][rx] = '.'
      rx, ry = rx+dx, ry+dy
  print_grid(grid)
  print("Part 1", sum(100 * y + x for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == 'O'))

  grid, instructions = read(lines)
  grid = large_grid(grid)
  rx, ry = find_robot(grid)
  for i in instructions:
    if i == '<' or i =='>':
      dx = inst[i][0]
      if move_horz(grid, rx+dx, ry, dx, '@'):
        grid[ry][rx] = '.'
        rx, ry = rx+dx, ry
    else:
      dy = inst[i][1]
      if can_move_vert(grid, rx, ry+dy, dy):
        grid[ry][rx] = '.'
        move_vert(grid, rx, ry+dy, dy, '@')
        rx, ry = rx, ry+dy
  print_grid(grid)
  print("Part 2", sum(100 * y + x for y in range(len(grid)) for x in range(len(grid[0])) if grid[y][x] == '['))
