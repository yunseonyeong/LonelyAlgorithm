import sys
i = 1

while True :
  answer = 0
  L, P, V = map(int, sys.stdin.readline().split())
  
  if L==0 :
    break

  if V % P >= L :
    answer += V//P*L + L
  else :
    answer += V//P*L + V % P

  print('Case {}: {} '.format(str(i), answer))
  i += 1

