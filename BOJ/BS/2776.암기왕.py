import sys
input = sys.stdin.readline

def bs(s, e, one, n):
  while s <= e :
    m = (s + e) // 2
    if one[m] == n :
      return 1
    elif one[m] > n :
      e = m - 1
    else :
      s = m + 1
  return 0

T = int(input())
for _ in range(T) :
  N = int(input())
  one = sorted(list(map(int, input().split())))
  M = int(input())
  two = list(map(int, input().split()))

  for n in two :
    print(bs(0,N-1, one, n))
