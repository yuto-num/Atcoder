import sys
import heapq, math, itertools
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
inputs = sys.stdin.readline
mod = 10**9+7
inf = float('inf')
#sys.setrecursionlimit(10**7)

def main():
  s = input()
  print('er' if s[::-1][:2]=='re' else 'ist')

if __name__ == '__main__':
  main()