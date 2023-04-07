import sys
import heapq
input = sys.stdin.readline 

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
  a,b,c = map(int, input().split())
  graph[a].append((c,b))
  graph[b].append((c,a))

def dijkstra(s,d):
  q = []
  heapq.heappush(q,(0,s))
  distance[s] = 0
  while q :
    dst, now = heapq.heappop(q)
    if distance[now] < dst :
      continue
    for i in graph[now]:
      cost = i[0] + dst
      if cost < distance[i[1]]:
        distance[i[1]] = cost
        heapq.heappush(q,(cost,i[1]))

  return distance[d]

answer = dijkstra(1,N)
print(answer)