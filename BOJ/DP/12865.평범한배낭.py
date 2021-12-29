import sys
input = sys.stdin.readline

N,K = map(int, input().split())
item = [[0]*2 for _ in range(N+1)]
back = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1) :
  item[i][0], item[i][1] = map(int, input().split())

for i in range(1, N+1) :
  w = item[i][0]
  v = item[i][1]
  for j in range(1,K+1) :
    if w <= j :
      back[i][j] = max(back[i-1][j], back[i-1][j-w] + v)
    else :
      back[i][j] = back[i-1][j]
print(back[N][K])
    

