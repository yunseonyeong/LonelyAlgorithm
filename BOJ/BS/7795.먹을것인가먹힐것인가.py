import sys
input = sys.stdin.readline
from bisect import bisect_right

T = int(input())

for _ in range(T):
  N,M = map(int, input().split())
  A = list(map(int, input().split()))
  B = sorted(list(map(int, input().split())))
  cnt = 0
  for a in A :
    cnt += bisect_right(B, a-1)
  print(cnt)





