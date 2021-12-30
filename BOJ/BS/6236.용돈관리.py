import sys
input = sys.stdin.readline
N,M = map(int, input().split())
money = []

for _ in range(N) :
  money.append(int(input()))

start = max(money)
end = sum(money)

result = 0
while start <= end :
  mid = (start + end) // 2
  have = 0
  cnt = 0
  for m in money :
    if have >= m :
      have -= m
    else :
      have = mid - m
      cnt += 1
  
  if cnt > M :
    start = mid + 1
  else :
    result = mid
    end = mid - 1

print(result)