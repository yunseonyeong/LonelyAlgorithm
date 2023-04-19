import sys
input = sys.stdin.readline

# 청소되지않은 빈칸 : 0
# 벽 : 1
# 청소된 빈칸 : 2

def backward(graph, r, c, d):
    if 0<=r<N-1 and d == 0:
        if graph[r+1][c] != 1:
            r = r+1
            return True, graph, r, c
    elif 0<=c<M+1 and d == 1:
        if graph[r][c-1] != 1:
            c = c-1
            return True, graph, r, c
    elif 0<=r<N+1 and d == 2:
        if graph[r-1][c] != 1:
            r = r-1
            return True, graph, r, c
    elif 0<=c<M-1 and d == 3:
        if graph[r][c+1] != 1:
            c = c+1
            return True, graph, r, c

    return False, graph, r, c

def rotate_forward(graph, r, c, d):
    if d == 0: # 북
        d = 3
        if 0<=c<M+1 and graph[r][c-1] == 0:
            c = c-1
    elif d == 1: # 동
        d = 0
        if 0<=r<N+1 and graph[r-1][c] == 0:
            r = r-1
    elif d == 2: # 남
        d = 1
        if 0<=c<M-1 and graph[r][c+1] == 0:
            c = c+1
    elif d == 3: # 서
        d = 2
        if 0<=r<N-1 and graph[r+1][c] == 0:
            r = r+1

    return graph, r, c, d

N,M = map(int, input().split())
r,c,d = map(int, input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0

for _ in range(N):
    graph.append(list(map(int, input().split())))

while True:
    cnt = 0
    if graph[r][c] == 0:
        graph[r][c] = 2
        answer += 1
    
    for i in range(4):
        nx = dx[i] + r
        ny = dy[i] + c
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
            cnt += 1
        
    if cnt > 0:
        graph,r,c,d = rotate_forward(graph, r, c, d)
    else:
        result,graph,r,c = backward(graph, r, c, d)
        if not result:
            break

print(answer)

