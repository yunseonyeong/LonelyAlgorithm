import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [[]for _ in range(N+1)]

def dijkstra(s):
  distance = [1000000]*(N+1)
  q = []
  heapq.heappush(q, (0,s))
  distance[s] = 0

  while q :
    dist,now = heapq.heappop(q)
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q,(cost,i[0]))

  return distance

for _ in range(1,N):
  parent, child, cost = map(int, input().split())
  graph[parent].append((child,cost))
  graph[child].append((parent,cost))


d = dijkstra(1)
d_index = d.index(max(d[1:]))
print(max(dijkstra(d_index)[1:]))
