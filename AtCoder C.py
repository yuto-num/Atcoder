import numpy as np

def main():
  n,m = map(int, input().split())
  b = [list(map(int, input().split())) for _ in range(n)]
  b = np.array(b)
  flg = True
  for i in range(m):
    if b[0][i]%7==0 and i!=m-1:
      flg = False
  for i in range(n):
    if m!=1 and set(np.diff(b[i]))!={1}:
      flg = False
  bt = b.T
  for i in range(m):
    if n!=1 and set(np.diff(bt[i]))!={7}:
      flg = False
  print('Yes' if flg else 'No')

if __name__ == '__main__':
  main()