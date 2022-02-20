import sys
from itertools import combinations
input = sys.stdin.readline

def chick_dst(chicks):
  total_dst = 0
  for homex, homey in home:
    mindst = sys.maxsize
    for chickx, chicky in chicks:
      dst = abs(homex-chickx) + abs(homey-chicky)
      if dst < mindst :
        mindst = dst
    total_dst += mindst
    
  return total_dst


N,M = map(int, input().split())
home = []
chicken = []
answer = sys.maxsize

for i in range(N):
  s = input().split()
  for j in range(N):
    if s[j] == '1':
      home.append([i,j])
    if s[j] == '2':
      chicken.append([i,j])

for chicks in list(combinations(chicken,M)):
  total_dst = chick_dst(chicks)
  if total_dst<answer:
    answer = total_dst

print(answer)
