from collections import deque

N,K = map(int, input().split())
cnt = 0
queue = deque()
queue.append((0,N))
visited = [False] * (1000001)
visited[N] = True

while queue:
  now = queue.popleft()
  if now[1] == K :
    print(now[0])
    break

  move = now[1]*2
  if move <= 100000 and not visited[move]:
    visited[move] = True
    queue.append((now[0],move))
  
  for n in (now[1]-1, now[1]+1):
    if 0<=n<=100000 and not visited[n]:
      visited[n] = True
      queue.append((now[0]+1, n))


  
