from re import M
import sys
input = sys.stdin.readline
import copy
sys.setrecursionlimit(10**6)

def dfs(g,x,y,h):
  dx = [1,-1,0,0]
  dy = [0,0,1,-1]
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    if (0<=nx<N) and (0<=ny<N) and g[nx][ny] > h :
      g[nx][ny] = -1
      dfs(g,nx,ny,h)

count = []
N = int(input())
graph = []
h = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

while h <= 100:
  graph2 = copy.deepcopy(graph)
  cnt = 0
  for i in range(N):
    for j in range(N):
      if graph2[i][j] > h :
        graph2[i][j] = -1
        cnt += 1
        dfs(graph2,i,j,h)      
  count.append(cnt)
  h += 1

print(max(count))
