import sys, heapq
input = sys.stdin.readline

M,N = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

def dijkstra():
    queue = []
    heapq.heappush(queue, (0,0,0))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    distance = [[1e9 for _ in range(M)] for _ in range(N)]
    distance[0][0] = 0
    while queue:
        cost, x, y = heapq.heappop(queue)
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<N and 0<=ny<M :
                if cost + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = cost + graph[nx][ny]
                    heapq.heappush(queue, (distance[nx][ny], nx, ny))
                    print(queue)

    return distance[N-1][M-1]

print(dijkstra())