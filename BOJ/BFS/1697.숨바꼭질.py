from collections import deque

N,K = map(int, input().split())
queue = deque()
queue.append((N,0))
visited = [False] * (100001)
visited[N] = True

while queue:
  now = queue.popleft()
  if now[0] == K :
    print(now[1])
    break
  
  for move in (now[0]*2, now[0]-1, now[0]+1):
    if 0 <= move <= 100000 and not visited[move]:
      queue.append((move,now[1]+1))
      visited[move] = True