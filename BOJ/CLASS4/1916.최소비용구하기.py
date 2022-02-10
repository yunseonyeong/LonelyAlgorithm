import sys
import heapq
input = sys.stdin.readline

N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수
graph = [[]*(N+1) for _ in range(N+1)]
INF = int(1e9)
distance = [INF]*(N+1)

for _ in range(M):
  s,f,d = map(int, input().split())
  graph[s].append((f,d))

ss,sd = map(int, input().split())

def dijkstra(s,d):
  q = []
  heapq.heappush(q, (0,s))
  distance[s] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist : continue
    for i in graph[now]:
      cost = dist + i[1]          # 선택된 노드로 가는 최소비용 + 선택된 노드를 거쳐 인접 노드(i)로 가는데 드는 비용(graph[i][1])
      if cost < distance[i[0]] :   # 원래 기록되어 있던 인접노드 i로 가는 비용보다 cost가 적다면 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))
  
  return distance[d]

result = dijkstra(ss,sd)
print(result)