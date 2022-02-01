import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):
  queue.append((x,y))
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  while queue :
    now = queue.popleft()
    graph[now[0]][now[1]] = -1
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<M) and graph[nx][ny] == 1:
        graph[nx][ny] = -1
        queue.append((nx,ny))

queue = deque()
T = int(input())
cnt = 0

for _ in range(T):
  M,N,K = map(int, input().split()) ## M : 가로, N:세로, K:배추 위치 개수
  graph = [[0]*(M) for _ in range(N)]
  for _ in range(K):
    a,b = map(int, input().split())
    graph[b][a] = 1

  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        bfs(i,j)
        cnt += 1

  print(cnt)
  cnt = 0