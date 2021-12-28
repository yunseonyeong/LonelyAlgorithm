import sys
input = sys.stdin.readline

N = int(input())
tile = [0] * (N+2)
tile[1] = 1
tile[2] = 2

for i in range(3,N+1) :
  tile[i] = (tile[i-1] + tile[i-2])%15746

print(tile[N])