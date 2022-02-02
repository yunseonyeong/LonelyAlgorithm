import sys
from collections import deque
input = sys.stdin.readline


def bfs(a):
  queue.append(a)
  while queue :
    now = queue.popleft()
    for n in graph[now] :
      if cnt[n] == 0:
        cnt[n] = cnt[now] + 1
        queue.append(n)

queue = deque() 
N = int(input())
a,b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
cnt = [0]*(N+1)

for _ in range(M):
  x,y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

bfs(a)
if cnt[b] == 0 : print(-1)
else : print(cnt[b])
