import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
  cnt = 1
  queue = deque([n])
  visited = [False] * (N+1)
  visited[n] = True

  while queue :
    cur = queue.popleft()
    for hack in graph[cur]:
      if visited[hack] == False:
        visited[hack] = True
        cnt += 1
        queue.append(hack)

  return cnt

N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
max_cnt = 1
answer = []

for _ in range(M):
  x,y = map(int, input().split())
  graph[y].append(x)


for n in range(1,N+1):
  cnt = bfs(n)
  
  if cnt > max_cnt :
    max_cnt = cnt
    answer.clear()
    answer.append(n)
  elif cnt == max_cnt :
    answer.append(n)

print(*sorted(answer))