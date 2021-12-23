import sys
input = sys.stdin.readline
cnt = 1
N = int(input())
nums = list(map(int, input().split()))    # 수 배열
dp = [1] * N        # 길이 배열

for i in range(1,N) :
  for j in range(i) :
    if nums[j] < nums[i] :
      dp[i] = max(dp[i], dp[j] + 1)       # dp[i]에는 이전의 max(dp[i], dp[j-1]+1) 값이 들어가 있기 때문에, 계속 업데이트 해주어야 한다.

print(max(dp))
