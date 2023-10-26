import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x,y):
    global cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<nx<N+1 and 0<ny<M+1 and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = True
                dfs(nx,ny)

N,M,K = map(int, input().split())
graph = [[0] * (M+1) for _ in range(N+1)]
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = []
visited = [[False] * (M+1) for _ in range(N+1)]

for _ in range(K):
    r,c = map(int, input().split())
    graph[r][c] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        if graph[i][j] == 1:
            cnt += 1
            visited[i][j] = True
            dfs(i,j)
            result.append(cnt)
            cnt = 0

print(max(result))