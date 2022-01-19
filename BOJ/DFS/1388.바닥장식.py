import sys
input = sys.stdin.readline

def dfs(x,y) :
  if x <= -1 or x >= N or y <= -1 or y >= M :
    return
  
  if tile[x][y] == '-' :
    tile[x][y] = 'X'
    try:
      if tile[x][y+1] == '-':
        dfs(x,y+1)
    except IndexError:
      pass

  if tile[x][y] == '|':
    tile[x][y] = 'X'
    try:
      if tile[x+1][y] == '|':
        dfs(x+1, y)
    except IndexError:
      pass
    
N,M = map(int, input().split())
tile = []

for _ in range(N) :
  tile.append(list(input().rstrip()))

count = 0

for i in range(N):
  for j in range(M):
    if tile[i][j] == '-' or tile[i][j] == '|':
      dfs(i, j)
      count += 1

print(count)