N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(2, N+1) :
  dp[i] = dp[i-1] + 1

  if dp[i] > dp[i//2] + 1 and i % 2 == 0:
    dp[i] = dp[i//2] + 1
  
  if dp[i] > dp[i//3] + 1 and i % 3 == 0:
    dp[i] = dp[i//3] + 1

print(dp[N])