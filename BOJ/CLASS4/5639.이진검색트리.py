import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def pretopost(arr):
  length = len(arr)

  if length <= 1:
    return arr

  for i in range(1,length):
    if arr[i] > arr[0] :
      result = pretopost(arr[1:i]) + pretopost(arr[i:]) + [arr[0]] 
      return result

  return pretopost(arr[1:]) + [arr[0]]

nums = []
while True:
  try:
    nums.append(int(input()))
  except:
    break
nums = pretopost(nums)

for n in nums:
  print(n)