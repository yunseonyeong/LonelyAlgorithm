import sys

T = int(sys.stdin.readline().strip())

def fibo(n,dp) :

  if n == 0 :
    dp[0][0] = 1
  if n == 1 :
    dp[1][1] = 1
  if dp[n][0] != 0 or dp[n][1] != 0:
    return dp[n]
  
  else :
    dp[n][0] = fibo(n-1,dp)[0] + fibo(n-2,dp)[0]
    dp[n][1] = fibo(n-1,dp)[1] + fibo(n-2,dp)[1]

  return dp[n]

for _ in range(T):
  n = int(sys.stdin.readline())
  
  dp = [[0,0] for _ in range(n+1)]

  answer = fibo(n,dp)

  print(answer[0], answer[1])
  
