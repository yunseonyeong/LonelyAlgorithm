import sys
input = sys.stdin.readline

def dfs(x,y) :
  if x <= -1 or x >= N or y <= -1 or y >= N or visited[x][y] == 1 :
    return

  if miro[x][y] == -1 :
    visited[x][y] = 1
    return

  visited[x][y] = 1
  
  dfs(x+miro[x][y], y)
  dfs(x, y+miro[x][y])

N = int(input())
miro = []

for _ in range(N) :
  miro.append(list(map(int, input().split())))

visited = [[0]*N for _ in range(N)]
dfs(0,0)

if visited[-1][-1] == 1 :
  print('HaruHaru')
else :
  print('Hing')