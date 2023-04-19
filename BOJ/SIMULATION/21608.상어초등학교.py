import sys
input = sys.stdin.readline

def select_seat(classroom, student, likes):
    blank_max = -1
    like_max = -1
    for i in range(N):
        for j in range(N):
            like_cnt = 0
            blank_cnt = 0
            if classroom[i][j] == 0:
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0<=nx<N and 0<=ny<N :
                        if classroom[nx][ny] in likes:
                            like_cnt += 1
                        elif classroom[nx][ny] == 0:
                            blank_cnt += 1

                if like_cnt > like_max or (like_cnt == like_max and blank_cnt > blank_max):
                    blank_max = blank_cnt
                    like_max = like_cnt
                    selected = (i,j)
    
    classroom[selected[0]][selected[1]] = student

def get_total(classroom):
    total = 0
    for i in range(N):
        for j in range(N):
            student = classroom[i][j]
            like = 0
            for k in range(4):
                nx= i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if classroom[nx][ny] in like_map[student]:
                        like += 1
            if like > 0:
                total += 10 ** (like-1)
    
    return total


N = int(input())
like_map = {}
classroom = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N**2):
    line = list(map(int, input().split()))
    like_map[line[0]] = line[1:]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for student, likes in like_map.items():
    select_seat(classroom, student, likes)

total = get_total(classroom)
print(total)