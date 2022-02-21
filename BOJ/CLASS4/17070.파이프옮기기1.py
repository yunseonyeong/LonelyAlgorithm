import sys

input = sys.stdin.readline
HORIZON = 0
VERTIC = 1
DIAGON = 2
N = int(input())
graph = []

for _ in range(N):
  graph.append(list(map(int, input().split())))

# def dfs(x,y,direction):
#   global cnt
#   if x == N-1 and y == N-1 :
#     cnt += 1

#   if direction == "horizon":
#     if y + 1 < N and graph[x][y+1] == 0:
#       dfs(x,y+1,"horizon")
#     if x + 1 < N and y + 1 < N and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
#         dfs(x+1,y+1,"diagonal") 

#   if direction == "vertical":
#     if x + 1 < N and graph[x+1][y] == 0:
#       dfs(x+1, y, "vertical")
#     if x + 1 < N and y + 1 < N and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
#       dfs(x+1,y+1,"diagonal") 

#   if direction == "diagonal":
#     if y + 1 < N and graph[x][y+1] == 0:
#       dfs(x,y+1,"horizon")
#     if x + 1 < N and graph[x+1][y] == 0:
#       dfs(x+1, y, "vertical")
#     if x + 1 < N and y + 1 < N and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
#       dfs(x+1,y+1,"diagonal")
  
# cnt = 0
# dfs(0,1,"horizon")

# print(cnt)

pipe = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

pipe[HORIZON][0][1] = 1

for i in range(2,N):
  if graph[0][i] == 0:
    pipe[HORIZON][0][i] = pipe[HORIZON][0][i-1]

for i in range(1,N):
  for j in range(2,N):
    if graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0:
      pipe[DIAGON][i][j] = pipe[VERTIC][i-1][j-1] + pipe[HORIZON][i-1][j-1] + pipe[DIAGON][i-1][j-1]
    if graph[i][j] == 0 :
      pipe[HORIZON][i][j] = pipe[HORIZON][i][j-1] + pipe[DIAGON][i][j-1]
      pipe[VERTIC][i][j] = pipe[VERTIC][i-1][j] + pipe[DIAGON][i-1][j]

print(pipe[VERTIC][N-1][N-1] + pipe[HORIZON][N-1][N-1] + pipe[DIAGON][N-1][N-1])