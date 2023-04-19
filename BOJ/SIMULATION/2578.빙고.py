import sys
input = sys.stdin.readline
bingo = []
answer = []
check = [[False for _ in range(5)] for _ in range(5)]

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    answer += list(map(int, input().split()))

def check_bingo():
    cnt = 0
    global check, bingo, answer
    for i in range(5):
        if check[i].count(True) == 5:
            cnt += 1
    
    for i in range(5):
        tmp = 0
        for j in range(5):
            if check[j][i] == True:
                tmp += 1
        if tmp == 5:
            cnt += 1

    tmp = 0

    for i in range(5):
        if check[i][i] == True:
            tmp += 1

    if tmp == 5:
        cnt += 1
    
    tmp = 0

    for i in range(5):
        if check[i][4-i] == True:
            tmp += 1

    if tmp == 5:
        cnt += 1

    return cnt

for k,a in enumerate(answer):
    for i in range(5):
        for j in range(5):
            if a == bingo[i][j]:
                check[i][j] = True

    if check_bingo() >= 3:
        print(k+1)
        break