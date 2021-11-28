N = int(input())
time = list(map(int, input().split()))

time.sort()
result = 0
wait = 0

for t in time :
  wait += t
  result += wait

print(result)