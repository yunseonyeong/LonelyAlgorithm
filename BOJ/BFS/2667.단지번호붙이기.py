import sys
input = sys.stdin.readline
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
  graph[x][y] = -1
  queue.append((x,y))
  cnt = 0
  while queue :
    now = queue.popleft()
    cnt += 1
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<N) and graph[nx][ny] == '1':
        graph[nx][ny] = -1
        queue.append((nx,ny))
        
  return cnt

N = int(input())
graph = []      # 전체 그래프

town = []       # 단지별 집의 수
queue = deque()

for _ in range(N):
  graph.append(list(input().rstrip()))

for i in range(N):
  for j in range(N):
    if graph[i][j] == '1':
      town.append(bfs(i,j))
      
town.sort()
print(len(town))
for t in town :
  print(t)