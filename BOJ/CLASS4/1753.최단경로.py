import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = int(1e9)
V,E = map(int, input().split())
K = int(input())
graph = [[]*(V+1) for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
  u,v,w = map(int, input().split())
  graph[u].append((v,w))

def dijkstra(s):
  q = []
  heapq.heappush(q, (0,s))
  distance[s] = 0
  while q :
    dist, now = heapq.heappop(q)
    if distance[now] < dist : continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
        
dijkstra(K)

for i in range(1,V+1):
  if distance[i] != INF :
    print(distance[i])
  else :
    print("INF")