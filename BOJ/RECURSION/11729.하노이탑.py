def hanoi(N,start,dest,via):
    if N == 1:
        move.append([start,dest])
    else :
        hanoi(N-1,start,via,dest)
        move.append([start,dest])
        hanoi(N-1,via,dest,start)  

N = int(input())
move = []
hanoi(N,1,3,2)
print(len(move))

for i in range(len(move)):
    print(move[i][0],move[i][1])