import sys
import heapq

N = int(sys.stdin.readline())
time = []
heap = []

for _ in range(N) :
  time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x: (x[0], x[1]))
heap.append(time[0][1])
cnt = 1

for t in time[1:] :
  if t[0] >= heap[0] :
    heapq.heappop(heap)
    heapq.heappush(heap, t[1])
  else :
    cnt += 1
    heapq.heappush(heap, t[1])

print(cnt)  

