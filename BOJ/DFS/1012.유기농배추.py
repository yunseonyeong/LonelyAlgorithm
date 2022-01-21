import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if (0<=nx<N) and (0<=ny<M) :
      if graph[nx][ny] == 1:        # 배추 존재할 때 1
        graph[nx][ny] = -1          # 지렁이 방문 처리 -1
        dfs(nx, ny)                   
  
T = int(input())

for _ in range(T) :
  M, N, K = map(int, input().split())
  graph = [[0]*M for _ in range(N)]
  cnt = 0

  for _ in range(K):
    X, Y = map(int, input().split())
    graph[Y][X] = 1                     # 배추 존재 1
  
  for i in range(N):
    for j in range(M):
      if graph[i][j] > 0:       # 지렁이가 아직 방문 x, 배추는 O
        dfs(i,j)
        cnt += 1                 # 상하좌우 탐색 끝나면 지렁이 +1

  print(cnt)
