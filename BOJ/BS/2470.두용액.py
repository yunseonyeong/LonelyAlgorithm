import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

s = 0
e = N-1
sval = 2000000000

while s < e :
  value = liquid[s] + liquid[e]
  if abs(value) <= abs(sval) :
    sval = value
    first = liquid[s]
    second = liquid[e]

  if value > 0 :
    e -= 1
  elif value < 0 :
    s += 1
  else :
    break

print(first, second)
  
  
  
  
