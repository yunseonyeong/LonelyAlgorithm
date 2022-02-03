import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b):
  queue.append(a)
  while queue :
    now = queue.popleft()
    for n in graph[now]:
      if cnt[n] == 0 :
        cnt[n] = cnt[now] + 1
        queue.append(n)
  return cnt[b]

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
cnt = [0]*(N+1)
result = [0]*(N+1)
queue = deque()
total = []
count = 0

for _ in range(M):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,N+1):
  cnt = [0] * (N+1)
  for j in range(1,N+1):
    if j != i :
      count = bfs(i,j)
      result[i] += count
  total.append(result[i])

tm = min(total)
for i,t in enumerate(total) :
  if t == tm :
    print(i+1)
    exit(0)
