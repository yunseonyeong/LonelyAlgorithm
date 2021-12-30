import sys
input = sys.stdin.readline

K,M = map(int, input().split())
LAN = []
for _ in range(K):
  LAN.append(int(input()))

start = 1
end = max(LAN)
result = 0

while start <= end :
  total = 0
  mid = (start + end) // 2

  for l in LAN :
    total += (l // mid)
    if total >= M :
      break

  if total >= M :
    result = mid
    start = mid + 1
  else :
    end = mid - 1
print(result)