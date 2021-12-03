# n번째 회의의 끝나는 시간 < n+1 번째 회의의 시작시간
# 회의가 빨리 끝날수록, 회의를 더 많이 잡을 수 있다.
import sys

N = int(input())
meets = []
cnt = 1

for _ in range(N) :
  meet= list(map(int, sys.stdin.readline().rstrip().split(" ")))
  meets.append(meet)

meets.sort(key=lambda x : (x[1],x[0]))

meet = meets[0][1]

for i in range(1,N) :
  if meets[i][0] >= meet :
    cnt += 1
    meet = meets[i][1]

print(cnt)


# 와 미친... 채점 시간 너무 너무 오래 걸려서 진짜 왜 그렇지 고민했는데, input() 이 진짜 시간이 많이 걸리는구나,, 괜히 낑낑댔네 
