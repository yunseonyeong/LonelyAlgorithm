import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**6

N,M = map(int, input().split())
graph = {}
visited = []

def dfs(n):
  for g in graph[n]:
    if g not in visited :
      visited.append(g)
      dfs(g)
      

for i in range(1,N+1):
  graph[i] = set()

for _ in range(M):
  u,v = map(int, input().split())
  graph[u].add(v)
  graph[v].add(u)
cnt = 0

for i in range(1,N+1):
  if i not in visited :
    dfs(i)
    cnt += 1
  
print(cnt)