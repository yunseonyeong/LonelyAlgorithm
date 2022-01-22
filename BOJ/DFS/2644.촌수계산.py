import sys
input = sys.stdin.readline

def dfs(p1):
  for n in graph[p1] :
    if visited[n] != True :
      if n == p2 :
        visited[n] = True
        cnt[n] = cnt[p1] + 1
        return
      visited[n] = True
      cnt[n] = cnt[p1] + 1
      dfs(n)

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

cnt = [0]*(n+1)
visited = [False] * (n+1)

dfs(p1)

if cnt[p2] == 0 :
  print(-1)
else :
  print(cnt[p2])