import sys
input = sys.stdin.readline
from collections import deque

def bfs():
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  while queue :
    now = queue.popleft()
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<M) and tomato[nx][ny] == 0 and visited[nx][ny] == False:
        visited[nx][ny] = True
        queue.append((nx,ny))
        tomato[nx][ny] = tomato[now[0]][now[1]] + 1
        
M,N = map(int, input().split())
tomato = []
queue = deque()
visited = [[False]*M for _ in range(N)]
day = 0

for _ in range(N):
  tomato.append(list(map(int, input().split())))

for i in range(N):
  for j in range(M):
    if tomato[i][j] == 1 :
      queue.append((i,j))
      visited[i][j] = True
bfs()
for tom in tomato :
  for t in tom :
    if t == 0 :
      print(-1)
      exit(0)
  day = max(day,max(tom))

print(day-1)