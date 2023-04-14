import sys
input = sys.stdin.readline
import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
route = [['-' for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    x,y,d = list(map(int, input().split()))
    graph[x].append((y,d))
    graph[y].append((x,d))
    route[x][y] = str(y)
    route[y][x] = str(x)

def dijkstra(s):
    global route
    distance = [1e9 for _ in range(n+1)]
    queue = []
    heapq.heappush(queue, (0, s))
    distance[s] = 0
    while queue:
        dist, node = heapq.heappop(queue)
        for no, d in graph[node]:
            if distance[no] > dist + d :
                distance[no] = dist + d
                heapq.heappush(queue, (distance[no], no))
                if node == s:
                    route[s][no] = no
                else:
                    route[s][no] = node
    return distance


for i in range(1, n+1):
    dijkstra(i)

def trace(i,j):
    r = j
    global route
    while True:
        if route[i][r] == r:
            return r
        
        r = route[i][r]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print('-', end=" ")
        else:
            print(trace(i,j), end=" ")
    print()

