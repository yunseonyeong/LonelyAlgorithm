import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
  global cnt
  queue.append(x)
  visited[x] = True
  while queue :
    now = queue.popleft()
    for c in connection[now]:
      if visited[c] == False:
        queue.append(c)
        visited[c] = True
        cnt += 1
  
N = int(input())
K = int(input())
connection = [[] for _ in range(N+1)]
queue = deque()
visited = [False]*(N+1)
cnt = 0

for _ in range(K):
  a,b = map(int, input().split())
  connection[a].append(b)
  connection[b].append(a)

bfs(1)
print(cnt)