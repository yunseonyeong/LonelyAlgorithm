import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
truer = deque(map(int, input().rstrip().split()[1:]))
parties = []
pair = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
  party = list(map(int, input().rstrip().split()))[1:]
  parties.append(party)
  for p in party:
    pair[p].extend(party.copy())
    pair[p].remove(p)

queue = truer.copy()

def bfs():
  while queue:
    now = queue.popleft()
    for p in pair[now]:
      if not visited[p]:
        visited[p] = True
        queue.append(p)
        truer.append(p)
  return truer

truerset = set(bfs())
cnt = 0
for party in parties:
  if not set(party).intersection(truerset):
    cnt +=1

print(cnt)