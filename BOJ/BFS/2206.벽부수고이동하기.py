import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))


def BFS():
    queue = deque()
    queue.append((0,0,0))
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    visited = [[[0,0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while queue:
        x,y,w = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0<=nx<N and 0<=ny<M and visited[nx][ny][w] == 0:
                if graph[nx][ny] == '1' and w == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx,ny,1))

                elif graph[nx][ny] == '0':
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append((nx,ny,w))
                        
    return -1

print(BFS())