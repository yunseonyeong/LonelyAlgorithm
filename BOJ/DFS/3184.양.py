import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    global o_cnt, v_cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<=nx<R and 0<=ny<C and graph[nx][ny] != '#' and not visited[nx][ny]:
            if graph[nx][ny] == 'o':
                o_cnt += 1
                
            elif graph[nx][ny] == 'v':
                v_cnt += 1

            visited[nx][ny] = True
            dfs(nx,ny)

R,C = map(int, input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
o_total = 0
v_total = 0
o_cnt = 0
v_cnt = 0
visited = [[False] * C for _ in range(R)]

for _ in range(R):
    graph.append(list(input().rstrip()))

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v':
            v_total += 1
        elif graph[i][j] == 'o':
            o_total += 1

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            visited[i][j] = True
            if graph[i][j] == 'o':
                o_cnt += 1
            elif graph[i][j] == 'v':
                v_cnt += 1
            dfs(i,j)
            if o_cnt > v_cnt :
                v_total -= v_cnt
            else:
                o_total -= o_cnt
            o_cnt = 0
            v_cnt = 0

print(o_total, v_total)