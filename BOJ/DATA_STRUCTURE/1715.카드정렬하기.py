import sys
input = sys.stdin.readline
import heapq

N = int(input())
heap = []
answer = 0
for _ in range(N):
    heapq.heappush(heap, int(input()))


while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    heapq.heappush(heap, one + two)

    answer += one + two

print(answer)