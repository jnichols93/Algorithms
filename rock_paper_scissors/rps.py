#!/usr/bin/python

import sys


options = {1:['rock'], 2:['paper'], 3:['scissors']}
if n == 0:
  return 0
if n == 1:
  return options
elif cache and cache[n] > 1:
  return cache[n]
else:
      if not cache:
    cache[n] = rock_paper_scissors(n, cache)
return cache[n]




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')