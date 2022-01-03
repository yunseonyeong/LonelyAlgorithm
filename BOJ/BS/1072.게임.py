import sys
input = sys.stdin.readline
from math import floor

X,Y = map(int, input().split())

Z = floor(Y*100/X)
start = 0
end = 1000000000
answer = []

if Z>=99 :
  print(-1)

else:
  while start <= end :
    mid = (start + end) // 2
    if floor((Y+mid)*100/(X+mid)) > Z :
      end = mid - 1
      answer.append(mid)
    else :
      start = mid + 1
  print(min(answer))
      
