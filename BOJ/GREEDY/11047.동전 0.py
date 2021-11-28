N, K = map(int, input().split())
coin = []
result = 0

for _ in range(N) :
  coin.append(int(input()))

coin.sort(reverse=True)

for c in coin:
  if c <= K :
    result += K//c
    K %= c

print(result)