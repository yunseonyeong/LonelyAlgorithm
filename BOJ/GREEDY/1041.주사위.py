import sys

N = int(sys.stdin.readline())
answer = 0
min_list = []
nums = list(map(int,(sys.stdin.readline().split())))

min_list.append(min(nums[0], nums[5]))
min_list.append(min(nums[1], nums[4]))
min_list.append(min(nums[2], nums[3]))

min_list.sort() 

one = min_list[0]
two = min_list[0] + min_list[1]
three = min_list[0] +min_list[1] + min_list[2]

if N == 1:
  answer = sum(nums) - max(nums)
else : 
  answer = three * 4 + two * 4 * (2*N-3) + one * (N-2)*(5*N-6)

print(answer)