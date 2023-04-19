import sys
input = sys.stdin.readline

def find_cleaner(graph, n):
    for i in range(n):
        if graph[i][0] == -1 :
            return i, i+1
        

def move_pollution(graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    result = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            cnt = 0
            if graph[i][j] > 0 :
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (0 <= nx < R) and (0 <= ny < C) and graph[nx][ny] != -1 :
                        cnt += 1
                        result[nx][ny] += graph[i][j]//5

                result[i][j] += graph[i][j] - graph[i][j]//5 * cnt

            
    result[top][0] = -1
    result[bottom][0] = -1

    return result

def clean_pollution(graph):
    # top down
    for i in range(top-1, 0, -1):
        graph[i][0] = graph[i-1][0]

    # top left
    for i in range(0, C-1):
        graph[0][i] = graph[0][i+1]
    graph[0][C-1] = graph[1][C-1]

    # top up
    for i in range(1, top):
        graph[i][C-1] = graph[i+1][C-1]

    # top right
    for i in range(C-1, 1, -1):
        graph[top][i] = graph[top][i-1]
    graph[top][1] = 0

    # bottom up
    for i in range(bottom+1, R-1):
        graph[i][0] = graph[i+1][0]
    graph[R-1][0] = graph[R-1][1]

    # bottom left
    for i in range(1, C-1):
        graph[R-1][i] = graph[R-1][i+1]
    graph[R-1][C-1] = graph[R-2][C-1]

    # bottom down
    for i in range(R-2, bottom, -1):
        graph[i][C-1] = graph[i-1][C-1]

    # bottom right
    for i in range(C-1, 1, -1):
        graph[bottom][i] = graph[bottom][i-1]
    graph[bottom][1] = 0

def get_pollution(graph):
    sum = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                sum += graph[i][j]
    return sum

R,C,T = map(int, input().split())
graph = []

for i in range(R):
    graph.append(list(map(int, input().split())))

top, bottom = find_cleaner(graph, R)

for _ in range(T):
    graph = move_pollution(graph)
    clean_pollution(graph)

answer = get_pollution(graph)
print(answer)