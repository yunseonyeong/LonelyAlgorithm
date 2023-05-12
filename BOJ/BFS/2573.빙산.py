import sys
input = sys.stdin.readline
from collections import deque

# 빙산 덩어리 개수를 세아리는 함수 1개 
# 빙산을 녹여버리는 함수 1개 
# 다 녹은건지 검사하는 함수 1개

def BFS(graph, x,y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny =  now[1] + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] != 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
    
def melt(graph):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    tmp = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            tmp[i][j] = graph[i][j]

    for x in range(1,N-1):
        for y in range(1,M-1):
            if graph[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                        cnt += 1
        
                tmp[x][y] = max(0, tmp[x][y] - cnt)
    
    return tmp


def zero(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                return False
            
    return True

N,M = map(int, input().split())
graph = []
answer = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))


while True:
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if not visited[i][j] and graph[i][j] != 0:
                BFS(graph, i,j)
                cnt += 1

                if cnt >= 2:
                    print(answer)
                    sys.exit(0)

    if zero(graph):
        print(0)
        break

    graph = melt(graph)
    answer += 1


