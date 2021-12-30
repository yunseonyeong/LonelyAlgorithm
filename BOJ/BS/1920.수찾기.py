import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

for num in nums :
  start = 0
  end = len(A)-1
  result = 0

  while start <= end :
    mid = (start + end)//2

    if A[mid] == num :
      result = 1
      break
    elif A[mid] > num :
      end = mid - 1
    elif A[mid] < num :
      start = mid + 1

  print(result)


