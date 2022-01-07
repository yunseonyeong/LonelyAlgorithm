import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()
result = [0] * 3
sval = 3000000000
for i in range(N-2) :
  if i > 0 and liquid[i] == liquid[i - 1]:
    continue
  s = i + 1
  e = N - 1

  while s < e :
    value = liquid[i] + liquid[s] + liquid[e]
    if abs(value) <= abs(sval) :
      sval = value
      result[0] = liquid[s]
      result[1] = liquid[e]
      result[2] = liquid[i]

    if value > 0 :
      e -= 1
    elif value < 0 :
      s += 1
    else :
      print(liquid[i], liquid[s], liquid[e])
      sys.exit(0)

result.sort()
result = [str(a) for a in result]
print(" " . join(result))