import sys
input = sys.stdin.readline

def compare_row_col():
    row_cnt, col_cnt, row_max, col_max = 1,1,1,1
    for i in range(N):
        for j in range(N-1):
            if graph[i][j] == graph[i][j+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    for j in range(N):
        for i in range(N-1):
            if graph[i][j] == graph[i+1][j]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1


    return max(row_max, col_max)


N = int(input())
graph = [0]*N
answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph[i] = list(input().strip())


for i in range(N):
    for j in range(N):
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if graph[i][j] != graph[nx][ny] :
                    graph[nx][ny], graph[i][j] = graph[i][j], graph[nx][ny]
                    answer = max(answer, compare_row_col())
                    graph[nx][ny], graph[i][j] = graph[i][j], graph[nx][ny]

print(answer)