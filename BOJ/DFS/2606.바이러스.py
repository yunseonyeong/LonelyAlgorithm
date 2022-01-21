import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def dfs(graph, v):
  for i in graph[v]:
    if i not in visited :
      visited.append(i)
      dfs(graph,i)

virus = {}
visited = []

for i in range(1,N+1) :
  virus[i] = set()

for _ in range(M) :
  a, b = map(int, input().split())
  virus[a].add(b)
  virus[b].add(a)

dfs(virus, 1)
print(len(visited)-1)