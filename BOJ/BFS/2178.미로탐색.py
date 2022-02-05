import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  queue.append((0,0))
  visited[0][0] = True
  cnt = [[0]*M for _ in range(N)]
  cnt[0][0] = 1
  
  while queue :
    now = queue.popleft()
    for i in range(4):
      nx = dx[i] + now[0]
      ny = dy[i] + now[1]
      if (0<=nx<N) and (0<=ny<M) and graph[nx][ny] == '1' and visited[nx][ny] == False:
        cnt[nx][ny] = cnt[now[0]][now[1]] + 1
        if nx == N-1 and ny == M-1 :
          return cnt[nx][ny]
        queue.append((nx,ny))
        visited[nx][ny] = True
  return cnt[N-1][M-1]

N,M = map(int, input().split())
graph = []
queue = deque()
visited = [[False]*M for _ in range(N)]

for _ in range(N) :
  graph.append(list(input().rstrip()))

print(bfs())