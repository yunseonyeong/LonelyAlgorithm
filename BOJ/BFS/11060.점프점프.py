import sys
input = sys.stdin.readline
from collections import deque

def bfs():
# 현재 위치 , 이동 가능 거리 
  queue = deque([(0,miro[0])])

  while queue : 
    location, howmuch = queue.popleft()
    for i in range(1,howmuch+1):
      if location + i < N and visited[location+i] == 0:     # 현재 가려는 곳이 아직 밟지 않은 곳이라면
        visited[location+i] = visited[location] + 1         # 점프한 곳에 현재까지 점프한 횟수가 찍힌다.
        queue.append((location+i, miro[location+i]))        # queue에 추가

  if not visited[N-1] :
    print(-1)
  else :
    print(visited[-1])

N = int(input())
miro = list(map(int, input().split()))
visited = [0] * N

if N == 1 :
  print(0)
else :
  bfs()