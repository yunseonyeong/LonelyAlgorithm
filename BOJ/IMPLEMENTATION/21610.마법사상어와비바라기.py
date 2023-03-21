import sys
input = sys.stdin.readline

def move_cloud(d,s,x,y):
    if d == 1:
        y -= s % N
    elif d == 2:
        x -= s % N
        y -= s % N
    elif d == 3:
        x -= s % N
    elif d == 4:
        y += s % N
        x -= s % N
    elif d == 5:
        y += s % N
    elif d == 6:
        x += s % N
        y += s % N
    elif d == 7:
        x += s % N
    elif d == 8:
        x += s % N
        y -= s % N
    
    return [(x+N)%N, (y+N)%N]

def rain(graph, clouds):
    cloud_cnt = [0 for _ in range(len(clouds))]
    dx = [-1, 1, -1, 1]
    dy = [1, -1, -1, 1]

    for cloud in clouds: 
        graph[cloud[0]][cloud[1]] += 1

    for i, cloud in enumerate(clouds):    
        for j in range(4):
            nx = cloud[0] + dx[j]
            ny = cloud[1] + dy[j]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > 0 :
                cloud_cnt[i] += 1
    for i, cnt in enumerate(cloud_cnt):
        graph[clouds[i][0]][clouds[i][1]] += cnt
    
    return graph

def make_new_clouds(graph, clouds):
    new_clouds = []
    visited = [[False for _ in range(N)]for _ in range(N)]

    for cloud in clouds:
            visited[cloud[0]][cloud[1]] = True

    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and [i,j] and not visited[i][j]:
                new_clouds.append([i, j])
                graph[i][j] -= 2

    return graph, new_clouds

def rain_sum(graph):
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += graph[i][j]
    
    return sum

N,M = map(int, input().split())
graph = []
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

for _ in range(N):
    graph.append(list(map(int, input().split())))

for _ in range(M):
    d,s = map(int,input().split())
    new_clouds = []
    for cloud in clouds:
        # 구름 1개씩 좌표 옮기기
        new_clouds.append(move_cloud(d,s,cloud[0],cloud[1]))
    
    clouds = new_clouds
    graph = rain(graph, clouds)
    graph, clouds = make_new_clouds(graph, clouds)

answer = rain_sum(graph)
print(answer)