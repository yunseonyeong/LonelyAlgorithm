import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
 
  dx = [-1,0,1,0,-1,-1,1,1]
  dy = [0,1,0,-1,-1,1,-1,1]
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
  
    if (0<=nx<h) and (0<=ny<w):
      if graph[nx][ny] == 1: # 방문처리
        graph[nx][ny] = -1
        dfs(nx, ny)



while True :
  w,h = map(int, input().split())
  if not w and not h:
    break
  graph = []
  cnt = 0
  for _ in range(h):
    graph.append(list(map(int, input().split())))

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        cnt += 1
        graph[i][j] = -1
        dfs(i,j)
        
  print(cnt)