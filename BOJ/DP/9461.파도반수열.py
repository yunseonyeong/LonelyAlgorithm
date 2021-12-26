import sys
input = sys.stdin.readline

T = int(input())

def sol(N, nums) :
  if N <= 5 : 
    return nums[N-1]
  else :
    for i in range(N-5) :
      newnum = nums[-1] + nums[-5]
      nums.append(newnum)
    return nums[N-1]

for _ in range(T) :
  nums = [1,1,1,2,2]
  t = int(input())
  print(sol(t, nums))

