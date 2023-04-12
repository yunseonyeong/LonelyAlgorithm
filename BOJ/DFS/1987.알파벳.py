import sys
input = sys.stdin.readline

def DFS(x,y,cnt):
    global result
    result = max(cnt, result)
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    for i in range(4):
        nx = x + direction[i][0]
        ny = y + direction[i][1]

        if 0<=nx<R and 0<=ny<C and not visited[graph[nx][ny]]:
            visited[graph[nx][ny]] = True
            DFS(nx,ny,cnt+1)
            visited[graph[nx][ny]] = False

R,C = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input().strip()))

for i in range(R):
    for j in range(C):
        graph[i][j] = ord(graph[i][j])-65

visited = [False for _ in range(26)]
visited[graph[0][0]] = True
result = 0
DFS(0,0,1)
print(result)