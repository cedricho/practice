# https://adventofcode.com/2025/day/8

import itertools as it
import math
import numpy as np
import sys


def read(file):
  get_coord = lambda line: np.array([int(i) for i in line.split(',')])
  with open(file) as input:
    return {i: get_coord(line.strip()) for i, line in enumerate(input)}


def dist(a, b):
  ka, va = a
  kb, vb = b
  dist = int(sum((va - vb) ** 2))
  return (dist, ka, kb)


def clustering(boxes, max_steps=-1):
  dist_boxes = [dist(a, b) for a, b in it.combinations(boxes.items(), 2)]
  dist_boxes.sort(key=lambda a: a[0])
  clusters = [[i] for i in range(len(boxes))]
  step = 0
  limits = range(max_steps) if max_steps > 0 else range(len(dist_boxes))
  for step in limits:
    _, a, b = dist_boxes[step]
    new_clusters = []
    cluster_a, cluster_b = [], []
    for cluster in clusters:
      if a in cluster:
        cluster_a = cluster
      elif b in cluster:
        cluster_b = cluster
      else:
        new_clusters.append(cluster)
    new_clusters.append(cluster_a + cluster_b)
    clusters = new_clusters
    if max_steps < 0 and len(clusters) == 1:
      # Answer for part 2
      return boxes[a][0] * boxes[b][0]

  clusters.sort(key=len, reverse=True)
  # Answer for part 1
  return math.prod(len(c) for c in clusters[:3])


def part1(file, max_steps):
  return clustering(read(file), max_steps)


def part2(file):
  return clustering(read(file), -1)


print("Part 1:", part1(sys.argv[1], int(sys.argv[2])))
print("Part 2:", part2(sys.argv[1]))