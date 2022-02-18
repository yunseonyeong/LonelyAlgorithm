# nPm, 중복 허용, 오름차순

from math import perm
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
result = []
def permutation(n,m,level,idx):
  if level == m :
    print(' '.join(map(str,result)))
    return
  for i in range(idx-1, N):
    result.append(i+1)
    permutation(n,m,level+1, i+1)
    result.pop()

permutation(N,M,0,1)