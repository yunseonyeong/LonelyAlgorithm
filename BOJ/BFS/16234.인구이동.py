import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y) :
  global is_move
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  cnt = 1
  queue.append((x,y))
  visited[x][y] = True
  total = graph[x][y]
  total_index = list()
  total_index.append((x,y))
  while queue :
    a,b = queue.popleft()
    for i in range(4):
      nx = dx[i] + a
      ny = dy[i] + b
      if nx<0 or ny<0 or N<=nx or N<=ny :
        continue
      if visited[nx][ny]:
        continue
      if (L<=abs(graph[nx][ny]-graph[a][b])<=R):
        visited[nx][ny] = True
        total+=graph[nx][ny]
        cnt += 1
        queue.append((nx,ny))
        total_index.append((nx,ny))

  newval = total//cnt

  if cnt > 1:
    is_move = True
    for a,b in total_index:
      graph[a][b] = newval
  
answer = 0
N,L,R = map(int, input().split())
graph = []
queue = deque()
visited = [[False]*N for _ in range(N)]

for _ in range(N):
  graph.append(list(map(int, input().split())))

while True:
  is_move = False
  visited = [[False]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False:
        bfs(i,j)  
  if is_move :
    answer += 1
  else:
    break

print(answer)
