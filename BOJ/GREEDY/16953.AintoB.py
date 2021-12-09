# 만약 B의 끝자리가 1이면 마지막 연산이 1을 붙인것 
# 만약 B의 끝자리가 1이 아닌 짝수이면 마지막 연산은 2를 곱한것 

# 반대로 생각해보면, B의 끝자리가 1이면 1을 떼고, 1이 아닌 짝수면 나누기 2를 해서 거꾸로 A를 구하자. 
# 1을 뗄때에는 일의자리 수는 10으로 나눈 나머지임을 이용한다. 

import sys

A,B = map(int,sys.stdin.readline().split())
cnt = 1

while True :
  if A == B :
    break
  elif (B % 10 != 1 and B % 2 != 0) or A > B :
    cnt = -1
    break
  elif B % 2 == 0 :
    B //=2
    cnt += 1
  elif B % 10 == 1 :
    B //= 10
    cnt += 1

print(cnt)
  
