import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
graph = [[0]*(N) for _ in range(M)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
result =[]

def dfs(x,y):
  global cnt
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if (0<=nx<M) and (0<=ny<N):
      if graph[nx][ny] == 0 :
        graph[nx][ny] = 1
        cnt += 1
        dfs(nx, ny)
        
for _ in range(K):
  x1, y1, x2, y2 = map(int, input().split())
  for i in range(y1, y2):
    for j in range(x1, x2):
      graph[i][j] = 1

for i in range(M):
  for j in range(N):
    if graph[i][j] == 0 :
      graph[i][j] = 1
      cnt += 1
      dfs(i,j)
      result.append(cnt)
      cnt = 0
      

print(len(result))
print(' '.join(map(str, sorted(result))))