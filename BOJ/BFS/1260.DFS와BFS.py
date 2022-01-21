import sys
from collections import deque 
input = sys.stdin.readline

def dfs(v):
  print(v, end=' ')
  visited[v] = True
  for i in graph[v]:
    if not visited[i] :
      dfs(i)

def bfs(v):
  visited[v] = True
  queue = deque([v])
  while queue :
    n = queue.popleft()
    print(n, end=' ')
    for i in graph[n]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,N+1):
  graph[i].sort()

dfs(V)
visited = [False] * (N+1)
print()
bfs(V)
