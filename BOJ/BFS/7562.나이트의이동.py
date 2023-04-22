import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
direction = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

def BFS(cur, mov):
    queue = deque()
    queue.append(cur)
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    
    while queue:
        lenq = len(queue)
        for _ in range(lenq):
            curx, cury = queue.popleft()
            if (curx, cury) == mov:
                return cnt
            for i in range(8):
                nx = curx + direction[i][0]
                ny = cury + direction[i][1]

                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        cnt += 1

for _ in range(T):
    N = int(input())
    curx, cury = map(int, input().split())
    movx, movy = map(int, input().split())
    print(BFS((curx,cury), (movx,movy)))
