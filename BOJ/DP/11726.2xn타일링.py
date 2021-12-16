import sys
sys.setrecursionlimit(10**6)
n = int(input())

dp = [0 for _ in range(n+1)]

def sol(n) :
  if dp[n] != 0 :
    return dp[n]
  if n == 1:
    return 1
  if n == 2:
    return 2
  dp[n] = sol(n-1) + sol(n-2)
  return dp[n] % 10007

print(sol(n))