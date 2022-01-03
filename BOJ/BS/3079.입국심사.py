import sys
input = sys.stdin.readline

N,M = map(int, input().split()) # N : 심사대 수 M : 사람 수
T = []
for _ in range(N):
  T.append(int(input()))
s = 0
e = max(T) * M  # 모두 다 제일 오래 걸리는 심사대에서 받는다고 했을 때, 최대 소요 시간
answer = []
while s <= e :
  m = (s + e) // 2
  cnt = 0
  for t in T :
    cnt += m // t
  if cnt >= M :
    e = m - 1
    answer.append(m)
  else:
    s = m + 1
print(min(answer))  
