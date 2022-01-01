import sys
input = sys.stdin.readline 

N = int(input())

budget = list(map(int, input().split()))
maxsum = int(input())

start = 0
end = max(budget)
answer = []
while start <= end :
  mid = (start + end) // 2
  result = 0
  for b in budget :
    if b <= mid :
      result += b
    else :
      result += mid
  
  if result <= maxsum :
    start = mid + 1
    answer.append(mid)
  else :
    end = mid - 1

print(max(answer))
