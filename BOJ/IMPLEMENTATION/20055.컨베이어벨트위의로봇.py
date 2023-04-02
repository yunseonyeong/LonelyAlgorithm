import sys
input = sys.stdin.readline

def move_belt(belt):
    tmp = belt[0][N-1]
    
    for i in range(N-1, 0, -1):
        belt[0][i] = belt[0][i-1]
    
    belt[0][0] = belt[1][0]

    for i in range(N-1):
        belt[1][i] = belt[1][i+1]

    belt[1][N-1] = tmp
    robot_down(belt)

    return belt
        
def robot_down(belt):
    if belt[0][N-1][0] :
        belt[0][N-1][0] = 0

def move_robot(belt):
    for i in range(N-2, -1, -1):
        if belt[0][i][0]:
            if not belt[0][i+1][0] and belt[0][i+1][1] >= 1:
                belt[0][i+1][1] -= 1
                belt[0][i+1][0] = 1
                belt[0][i][0] = 0

        robot_down(belt)

    return belt

def count_zero(belt):
    cnt = 0
    for i in range(2):
        for j in range(N):
            if belt[i][j][1] == 0:
                cnt += 1

    if cnt >= K:
        return True

    return False


N,K = map(int, input().split())
durability = list(map(int, input().split()))
belt = [[] for _ in range(2)]
answer = 0

for i in range(N):
    belt[0].append([0,durability[i]])
for i in range(2*N-1, N-1, -1):
    belt[1].append([0, durability[i]])

while True :
    answer += 1
    belt = move_belt(belt)
    belt = move_robot(belt)
    if belt[0][0][1]:
        belt[0][0][0] = 1
        belt[0][0][1] -= 1

    if count_zero(belt) :
        break
print(answer)