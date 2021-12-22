import sys
N = int(input())
stairs = []

for _ in range(N) :
  s = int(sys.stdin.readline().strip())
  stairs.append(s)

up = [0] * (N+1)

if N == 1:
  up[0] = stairs[0]
if N == 2:
  up[0] = stairs[0]
  up[1] = stairs[0] + stairs[1]
if N >= 3:
  up[0] = stairs[0]
  up[1] = stairs[0] + stairs[1]
  up[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

if N>=4 :
  for i in range(3,N) :
    up[i] = max(up[i-2] + stairs[i], up[i-3] + stairs[i-1] + stairs[i])

print(up[N-1])