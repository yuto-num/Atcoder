from collections import defaultdict
n,k = map(int, input().split())
a = list(map(int, input().split()))
cs = [0 for _ in range(n+1)]
for i in range(n):
  cs[i+1] = cs[i] + a[i]
cnt = defaultdict(int)
for x in cs[1:]:
  cnt[x] += 1
ans = 0
mns = 0
for x in a:
  ans += cnt[k+mns]
  cnt[x+mns] -= 1
  mns += x
print(ans)
