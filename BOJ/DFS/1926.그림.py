import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
  queue.append((x,y))
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  area = 1
  while queue :
    now = queue.popleft()
    graph[now[0]][now[1]] = -1
    
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]

      if (0<=nx<n) and (0<=ny<m) and (graph[nx][ny] > 0)  :
        graph[nx][ny] = -1        # 방문 처리
        queue.append((nx,ny))
        area += 1
  
  return area


n,m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

queue = deque()
cnt = 0
area_list = []

for i in range(n):
  for j in range(m):
    if graph[i][j] > 0 :
      area_list.append(bfs(i,j))
      cnt += 1

print(cnt)

if len(area_list) > 0 :
  print(max(area_list))
else :
  print(0)