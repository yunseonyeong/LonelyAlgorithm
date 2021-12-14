N = int(input())

bag = [N+1 for _ in range(N+4)]
bag[3] = 1
bag[5] = 1

for i in range(6,N+4):
  
  if bag[i-3] != N+1 or bag[i-5] != N+1 :
    if bag[i-3] == -1 and bag[i-5] != -1 :
      bag[i] = bag[i-5] + 1
    elif bag[i-3] != -1 and bag[i-5] == -1 :
      bag[i] = bag[i-3] + 1
    else:
      bag[i] = min(bag[i-3], bag[i-5]) + 1

  else :
    bag[i] = -1
bag[4] = -1    

print(bag[N])
