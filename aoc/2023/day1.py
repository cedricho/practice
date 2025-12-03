import re
import sys


def overlapping_match(text):
  digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
            'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
            '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
  pattern = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
  match = re.search(pattern, text)
  while match:
    yield digits[match.group()]
    text = text[match.start() + 1:]
    match = re.search(pattern, text)


# Open a file specified by the first command-line argument
with open(sys.argv[1]) as f:
  lines = [line.strip() for line in f.readlines()]

  groups = [re.findall(r'(\d)', line) for line in lines]
  print('Part 1', sum(int(group[0] + group[-1]) for group in groups))
  
  groups = [list(overlapping_match(line)) for line in lines]
  print('Part 2', sum(int(g[0] + g[-1]) for g in groups))
