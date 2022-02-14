A,B,C = map(int, input().rstrip().split())

def npower(a,b,c):
  if b == 1:
    return a % c
  else :
    if b % 2 == 0 : # 짝수
      reminder = npower(a,b//2,c)
      return (reminder * reminder) % c
    else :   # 홀수
      reminder = npower(a,b//2,c)
      return (reminder*reminder*a)%c

print(npower(A,B,C))