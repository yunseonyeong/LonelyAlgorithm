import sys
input = sys.stdin.readline

N,M = map(int, input().split())
course = list(map(int, input().split()))

start = max(course)
end = sum(course)
answer = []
while start <= end :
  mid = (start + end) // 2  # 정해진 합계 맥스값
  cnt = 0  # 블루레이 수
  blue = 0  # 현재 블루레이당 합계
  for c in course :
    if c + blue > mid :
      cnt += 1
      blue = c
    else :
      blue += c
  if (cnt+1) <= M :
    end = mid - 1
    answer.append(mid)
  else :
    start = mid + 1

print(min(answer))