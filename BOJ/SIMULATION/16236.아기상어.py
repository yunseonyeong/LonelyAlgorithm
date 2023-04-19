import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y,m,a,t):
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue.append((x,y))
    visited[x][y] = True
    direction = [(0,1), (0,-1), (1,0), (-1,0)]

    while queue:
        lenq = len(queue)
        tmp = (N,N)
        for _ in range(lenq):
            now = queue.popleft()
            for i in range(4):
                nx = direction[i][0] + now[0]
                ny = direction[i][1] + now[1]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] <= m:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    if graph[nx][ny] < m and graph[nx][ny] != 0:
                        if nx < tmp[0] or (nx == tmp[0] and ny < tmp[1]):
                            tmp = (nx,ny)
        
        t += 1

        if tmp != (N,N):
            a += 1
            graph[tmp[0]][tmp[1]] = 9
            graph[x][y] = 0
            
            if m == a:
                m += 1
                a = 0

            return True, tmp[0], tmp[1], m, a, t
        
    return False, tmp[0], tmp[1], m, a, t

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            graph[i][j] = 0
            x,y = i,j

result, x,y,m,a,t = bfs(x,y,2,0,0)
answer = 0

while True:
    if result:
        answer = t
        result, x, y, m, a, t = bfs(x,y,m,a,t)

    if not result :
        break

print(answer)