import sys
input = sys.stdin.readline
from collections import deque

def BFS(q):
    global graph, green, time
    direction = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]
    
    while q:
        if green == 0:
            return time

        lenq = len(q)
        for _ in range(lenq):
            h,x,y = q.popleft()

            for i in range(6):

                nh = h + direction[i][0]
                nx = x + direction[i][1]
                ny = y + direction[i][2]

                if 0<=nh<H and 0<=nx<N and 0<=ny<M and graph[nh][nx][ny] == 0:
                    graph[nh][nx][ny] = 1
                    green -= 1
                    q.append((nh,nx,ny))

        time += 1

    return -1
    
graph = []
M,N,H = map(int, input().split())
green = 0
queue = deque()
time = 0

for _ in range(H):
    stair = []
    for _ in range(N):
        stair.append(list(map(int, input().split())))

    graph.append(stair)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
            elif graph[i][j][k] == 0:
                green += 1

if green == 0:
    print(0)
else:
    print(BFS(queue))
