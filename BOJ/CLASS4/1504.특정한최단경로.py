import sys, heapq
input = sys.stdin.readline

N,E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [1e9 for _ in range(N+1)]
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        if node == end:
            return dist
        # 인접노드 탐색
        for n, d in graph[node]:
            if distance[n] > dist + d:
                distance[n] = dist + d
                heapq.heappush(queue, (distance[n], n))

    return distance[end]
    
dist_v1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
dist_v2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if dist_v1 >= 1e9 or dist_v2 >= 1e9:
    print(-1)
else:
    print(min(dist_v1, dist_v2))