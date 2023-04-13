import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

def spread(q, blank):
    time = 0
    direction = [(0,1), (0,-1), (1,0), (-1,0)]
    while True:
        lenq = len(q)
        # 바이러스가 모두 퍼지면
        if blank == 0:
            return time
        
        elif lenq == 0:
            return 1e9

        # 1초동안 활성 바이러스 퍼트리기
        for _ in range(lenq):
            x,y = q.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + direction[i][0]
                ny = y + direction[i][1]
                
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] :
                    if graph[nx][ny] == 0:
                        blank -= 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    
                    elif graph[nx][ny] == 2:
                        q.append((nx, ny))
                        visited[nx][ny] = True
        
        time += 1

N,M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

M_map = []
M_list = []
blank_cnt = 0
answer = 1e9
for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            blank_cnt += 1
        elif graph[i][j] == 2:
            M_list.append((i,j))

M_map = combinations(M_list, M)

# 가능한 활성 바이러스 M개의 조합에 대해서 BFS 진행하기
for m in M_map:
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    blank = blank_cnt
    for active in m:
        queue.append(active)

    stime = spread(queue, blank)
    answer = min(answer, stime)
    
if answer == 1e9:
    print(-1)
else:
    print(answer)
