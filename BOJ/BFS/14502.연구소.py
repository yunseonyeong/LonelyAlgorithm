import sys
import copy
from collections import deque 
input = sys.stdin.readline 

def bfs():
  global max_r
  result = 0
  visited = [[False]*M for _ in range(N)]
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  cop = copy.deepcopy(graph)
  queue = deque()

  for v in virus :
    queue.append(v)

  while queue:
    now = queue.popleft()
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<M) and cop[nx][ny] == 0 and visited[nx][ny] == False:
        cop[nx][ny] = 2
        visited[nx][ny] = True
        queue.append((nx,ny))
  
  for i in cop :
    for j in i :
      if j == 0 :
        result += 1

  max_r = max(max_r, result)
  
def wall(cnt):
  if cnt == 3:
    bfs()
    return

  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0 : 
        graph[i][j] = 1
        wall(cnt+1)
        graph[i][j] = 0


N,M = map(int, input().split())
graph = []
virus = []
max_r = 0

for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(M):
    if graph[i][j] == 2:
      virus.append((i,j))

wall(0)
print(max_r)