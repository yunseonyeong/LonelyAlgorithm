import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def RGsame(x,y):
  if graph[x][y] == 'R' or graph[x][y] == 'G':
    graph[x][y] = -1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if (0<=nx<N) and (0<=ny<N) and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G') :
        RGsame(nx,ny)

  if graph[x][y] == 'B':
    graph[x][y] = -1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if (0<=nx<N) and (0<=ny<N) and graph[nx][ny] == 'B':
        RGsame(nx,ny)

def RGdif(x,y):
  if graph2[x][y] == 'R':
    graph2[x][y] = -1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if (0<=nx<N) and (0<=ny<N) and graph2[nx][ny] == 'R':
        RGdif(nx,ny)

  if graph2[x][y] == 'G':
    graph2[x][y] = -1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if (0<=nx<N) and (0<=ny<N) and graph2[nx][ny] == 'G':
        RGdif(nx,ny)

  if graph2[x][y] == 'B':
    graph2[x][y] = -1
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if (0<=nx<N) and (0<=ny<N) and graph2[nx][ny] == 'B':
        RGdif(nx,ny)

N = int(input())
graph = []
for _ in range(N):
  graph.append(list(input().rstrip())) 

graph2 = copy.deepcopy(graph)
RGcnt = 0 
cnt = 0 

for i in range(N): 
  for j in range(N): 
    if graph[i][j] == 'R' or graph[i][j] == 'G' or graph[i][j] == 'B': 
      RGsame(i,j)
      RGcnt += 1

for i in range(N): 
  for j in range(N): 
    if graph2[i][j] == 'R' or graph2[i][j] == 'G' or graph2[i][j] == 'B': 
      RGdif(i,j)
      cnt += 1 

print(cnt,RGcnt)
