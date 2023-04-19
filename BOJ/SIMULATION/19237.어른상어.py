import sys
input = sys.stdin.readline

def update_smell():
    # smell[[상어번호, 냄새지속시간], [상어번호, 냄새지속시간],,,,]
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if shark[i][j] != 0:
                smell[i][j] = [shark[i][j], K]

def move_shark(shark):
    new_shark = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if shark[i][j] > 0:
                no_smell = False
                # 상어의 현재 방향에 맞는 우선순위 고르기
                # priority[상어번호][현재상어방향]
                for p in priority[shark[i][j]][direction[shark[i][j]]]:
                    nx = ds[p][0] + i
                    ny = ds[p][1] + j
                    if 0<=nx<N and 0<=ny<N :
                        if smell[nx][ny][1] == 0:
                            direction[shark[i][j]] = p
                            if new_shark[nx][ny] == 0:
                                new_shark[nx][ny] = shark[i][j]
                            else:
                                if shark[i][j] < new_shark[nx][ny]:
                                    direction[new_shark[nx][ny]] = -1
                                    new_shark[nx][ny] = shark[i][j]
                                else:
                                    direction[shark[i][j]] = -1

                            no_smell = True
                            break
                
                if no_smell:
                    continue

                for p in priority[shark[i][j]][direction[shark[i][j]]]:
                    nx = ds[p][0] + i
                    ny = ds[p][1] + j
                    if 0<=nx<N and 0<=ny<N and smell[nx][ny][0] == shark[i][j]:
                        direction[shark[i][j]] = p
                        new_shark[nx][ny] = shark[i][j]
                        break
    return new_shark

def finish_move(direction):
    cnt = 0
    print(direction)
    for d in direction:
        if d == -1:
            cnt += 1
    if cnt == M-1:
        return True
    return False

N,M,K = map(int, input().split())
priority = [[()for _ in range(5)] for _ in range(M+1)]
shark = []
smell = [[[0, 0]] * N for _ in range(N)]
ds = [(), (-1,0), (1,0), (0,-1), (0,1)]
time = 0
for _ in range(N):
    shark.append(list(map(int, input().split())))

direction = [0] + list(map(int, input().split()))
  
for i in range(1,M+1):
    for j in range(1,5):
        priority[i][j] = tuple(map(int, input().split()))

while True:
    update_smell()
    shark = move_shark(shark)
    time += 1

    if finish_move(direction):
        print(time)
        break
    
    if time >= 1000:
        print(-1)
        break