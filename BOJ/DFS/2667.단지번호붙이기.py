import sys
input = sys.stdin.readline

def dfs(x,y):
  global cnt
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
   
    if (0<=nx<N) and (0<=ny<N) :
      if graph[nx][ny] == '1':
        graph[nx][ny] = '-1'
        cnt += 1
        dfs(nx,ny)

N = int(input())
graph = []
cnt = 0
town = []

for _ in range(N):
  graph.append(list(input().rstrip()))

for i in range(N):
  for j in range(N):
    if graph[i][j] == '1':
      cnt += 1
      graph[i][j] = '-1'
      dfs(i,j)
      town.append(cnt)
      cnt = 0

town.sort()
print(len(town))
for t in town :
  print(t)