# 아 암만 봐도 먼 규칙인지 모르겠어서 결국 답지 봤는데 어이 없음 ㅠ 
# 그냥 몇 개 구해보면 되는거였어 
# f(n) = f(n-1) + f(n-2) + f(n-3) , n >= 4

T = int(input())
input_list = []

for i in range(T) :
  input_list.append(int(input()))

for t in input_list:
  dp = [1,2,4]
  for i in range(3, max(input_list)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
  print(dp[t-1])
