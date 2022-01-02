import sys
input = sys.stdin.readline
from bisect import bisect_left
N, H = map(int, input().split())
suck, jong = [], []

for _ in range(N // 2):
  suck.append(int(input()))
  jong.append(int(input()))
suck.sort()
jong.sort()
result = []
for h in range(1,H+1) :
  cnt = 0
  cnt += len(suck)-bisect_left(suck, h)
  cnt += len(jong)-bisect_left(jong, H-h+1)
  result.append(cnt)
m = min(result)
cnt = 0
for r in result :
  if r == m :
    cnt += 1

print(m,cnt)