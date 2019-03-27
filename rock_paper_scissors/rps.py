#!/usr/bin/python

import sys
import math

def rock_paper_scissors(n):
  answers = []
  iteration = 0
  options = ['rock', 'paper', 'scissors']

  while iteration < 3 ** n:
    permutation = [None] * n
    index = 1

    while index <= n:
      permutation[n - index] = options[math.floor(iteration / (3 ** (index - 1))) % 3]
      index += 1

    answers.append(permutation)
    iteration += 1

  return answers


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')