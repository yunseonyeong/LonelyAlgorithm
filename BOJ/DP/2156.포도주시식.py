import sys
input = sys.stdin.readline

N = int(input())
grape = [0]
dp = [0] * (N+1)

for _ in range(N) :
  grape.append(int(input()))

if N == 1 :
  print(grape[1])
  
if N == 2:
  print(grape[1]+grape[2])

if N == 3:
 print(max(grape[1]+grape[2], grape[1]+grape[3], grape[2] + grape[3]))

if N >= 4 :
  dp[1] = grape[1]
  dp[2] = grape[1] + grape[2]
  dp[3] = max(grape[1]+grape[2], grape[1]+grape[3], grape[2] + grape[3])

  for i in range(4,N+1):
    dp[i] = max(dp[i-1], dp[i-2] + grape[i], dp[i-3] + grape[i-1] + grape[i])

  print(max(dp))