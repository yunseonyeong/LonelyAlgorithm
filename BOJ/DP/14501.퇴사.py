import sys
input = sys.stdin.readline

N = int(input())
TP = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N-1, -1, -1) :
  if TP[i][0] + i  <= N :
    dp[i] = max(TP[i][1] + dp[i + TP[i][0]], dp[i+1])
  else :
    dp[i] = dp[i+1]
print(dp[0])
