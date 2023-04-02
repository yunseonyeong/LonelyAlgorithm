import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
rainbow = 0

def gravity(graph):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if graph[i][j] != -1:
                cur_row = i

                while cur_row + 1 < N and graph[cur_row+1][j] == -2:
                    graph[cur_row+1][j] = graph[cur_row][j]
                    graph[cur_row][j] = -2
                    cur_row += 1

    return graph

def rotate(graph):
    tmp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[N-j-1][i] = graph[i][j]

    return tmp

def remove_group(graph, blocks):
    for x,y in blocks:
        graph[x][y] = -2
    return graph

def find_group(x, y):
    queue = deque()
    queue.append((x,y))
    block_cnt = 1
    rainbow_cnt = 0
    blocks = [[x,y]]
    rainbows = []
    color = graph[x][y]

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<N :
                if graph[nx][ny] == color and not visited[nx][ny] :
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    block_cnt += 1
                    blocks.append([nx, ny])
                elif graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    rainbow_cnt += 1
                    rainbows.append([nx, ny])

    for i,j in rainbows:
        visited[i][j] = False

    return [block_cnt+rainbow_cnt, rainbow_cnt, blocks+rainbows]

N,M = map(int, input().split())
graph = []
score = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                group_info = find_group(i,j)
                if group_info[0] >= 2:
                    groups.append(group_info)

    groups.sort(reverse=True)
    if not groups:
        break

    graph = remove_group(graph, groups[0][2])
    score += groups[0][0] ** 2
    graph = gravity(graph)
    graph = rotate(graph)
    graph = gravity(graph)

print(score)