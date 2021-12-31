import sys
input = sys.stdin.readline

N = int(input())
card = sorted(list(map(int, input().split())))
M = int(input())
have = list(map(int, input().split()))

for h in have :
  start = 0
  result = 0
  end = len(card)-1
  while start <= end :
    mid = (start + end) // 2
    if h == card[mid] :
      result = 1
      break
    if h > card[mid] :
      start = mid + 1
    elif h < card[mid] :
      end = mid - 1
  
  print(result, end = ' ')


