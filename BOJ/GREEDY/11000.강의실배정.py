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

# 첫번째 풀이
# import sys
# from copy import deepcopy

# N = int(sys.stdin.readline())
# time = []
# for _ in range(N):
#   time.append(list(map(int, sys.stdin.readline().split())))

# time.sort(key=lambda x: (x[1], x[0]))      # 끝나는 시간을 우선적으로 오름차순 정렬함 

# end = [deepcopy(time[0][1]),]
# cnt = 1

# for t in time[1:]:
#   if t[0] < end[0] :              # end리스트는 항상 오름차순 정렬 되어 있으므로 가장 작은 값과 비교
#     cnt += 1                      # 시작 시간이 더 빠르면 같은 강의실 못 쓰므로 새 강의실 배정
#     end.append(t[1])

#   else :
#     del end[0]                    # 강의실 같이 쓸 수 있으므로 끝나는 시간 갱신
#     end.append(t[1])

# print(cnt)

# 위 풀이의 반례 : input => 4, (1,2) (1,4) (4,5) (2,6) 일 때, 
# (4,5)는 (1,4)와 같은 강의실을 쓰게 하고, (2,6)은 (1,2)와 같이 쓰게 해야 최솟값이 나오는데
# (4,5)를 (1,2)와 비교해 먼저 같은 강의실에 넣어버리니 (2,6)이 들어갈 수 없어 결과가 3이 되어 최적해를 도출하지 못한다.

# 위의 경우는 time리스트를 처음에 끝나는 시간을 우선적으로 정렬했기 때문인데,
# (1,2) (1,4) (2,6) (4,5) 이렇게 시작시간을 우선으로 정렬되어 있었다 하더라도 
# 끝나는 시간을 갱신하면서 계속 오름차순으로 sort해줘야 하므로 시간복잡도가 커지게 된다. 

# 따라서, 시작 시간을 우선으로 정렬한 뒤, heapq 를 이용해 heapq.heappop() 으로 min값을 꺼내줘서 비교해주어 위 두가지 문제를 모두 해결하였다. 