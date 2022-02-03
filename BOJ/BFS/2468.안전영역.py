import sys
from collections import deque
input = sys.stdin.readline
from copy import deepcopy

def bfs(x,y):
  queue.append((x,y))
  visited[x][y] = True
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  while queue :
    now = queue.popleft()
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<N) and visited[nx][ny] == False and graph[nx][ny] > h:
        visited[nx][ny] = True
        queue.append((nx,ny))

queue = deque()
N = int(input())
graph = []
h = 0
visited = [[False]*N for _ in range(N)]
cnt = 0
result = []

for _ in range(N):
  graph.append(list(map(int, input().split())))

while h <= 100 :
  cnt = 0
  for i in range(N):
    for j in range(N):
      if graph[i][j] > h and visited[i][j] == False: 
        cnt += 1
        bfs(i,j)
  result.append(cnt)
  h += 1
  visited = [[False]*N for _ in range(N)]

print(max(result))