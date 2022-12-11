import sys
import heapq, math, itertools
from collections import defaultdict, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right
inputs = sys.stdin.readline
mod = 10**9+7
inf = float('inf')
#sys.setrecursionlimit(10**7)

def main():
  n,m = map(int, inputs().split())
  b = [list(map(int, input().split())) for _ in range(n)]
  flg = True
  c = [x for x in b[0]]
  if len(c)>1:
    for i in range(1, len(c)):
      if not c[i]==c[i-1]+1:
        flg = False
      if not c[i]%7==c[i-1]%7+1:
        flg = False
    
  if n>1:
    for j in range(m):
      for i in range(1, n):
        if not b[i][j] == b[i-1][j]+7:
          flg = False
  print("Yes" if flg else 'No')

if __name__ == '__main__':
  main()