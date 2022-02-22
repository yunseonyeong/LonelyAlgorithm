from collections import deque

N,K = map(int, input().split())
queue = deque()
queue.append((N,0))
visited = [False] * 100001
cnt = 0
ways = []

while queue:
  now = queue.popleft()
  visited[now[0]] = True

  if now[0] == K :
    ways.append(now[1])
  
  for move in (now[0]*2, now[0]-1, now[0]+1):
    if 0 <= move <= 100000 and not visited[move]:
      queue.append((move,now[1]+1))
      
shortest = min(ways)

for way in ways:
  if way == shortest:
    cnt += 1

print(shortest)
print(cnt)