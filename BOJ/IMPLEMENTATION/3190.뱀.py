import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
# [위치, 방향]
graph = [[[0,-1] for _ in range(N)] for _ in range(N)]
changes = deque()

for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1][0] = 1

L = int(input())

for _ in range(L):
    s = input().split()
    sec, direction = int(s[0]), s[1]
    changes.append((sec, direction))

def rotate(d, cur):
    # 북, 서, 남, 동
    dd = [0,1,2,3]
    # 왼쪽으로 90도
    if d == 'L':
        return dd[(cur + 1) % 4]
    # 오른쪽으로 90도
    elif d == 'D':
        return dd[(cur - 1)]


def move(graph, head, tail, head_d, tail_d):
    direction = [(-1,0), (0,-1), (1,0), (0,1)]
    nx,ny = head[0] + direction[head_d][0], head[1] + direction[head_d][1]

    # 벽에 부딪히거나 몸통과 부딪히면 게임 오버
    if 0>nx or nx>=N or 0>ny or ny>=N or graph[nx][ny][0] == 2:
        return True, graph, tail, head
    
    else:
        # 머리 이동
        head = (nx, ny)
        # 이동한 곳에 사과가 있다면 머리만 이동
        if graph[nx][ny][0] == 1:
            graph[nx][ny] = [2, head_d]
        # 이동한 곳이 빈칸이라면 꼬리 이동
        elif graph[nx][ny][0] == 0:
            graph[nx][ny] = [2, head_d]
            graph[tail[0]][tail[1]] = [0,-1]
            # 꼬리 업데이트
            tail = (tail[0] + direction[tail_d][0], tail[1] + direction[tail_d][1])

    return False, graph, tail, head


cnt = 0
head = (0,0)
tail = (0,0)
gameover = False
graph[0][0] = [2,3]

while True:
    tail_d = graph[tail[0]][tail[1]][1]
    head_d = graph[head[0]][head[1]][1]
            
    if gameover:
        print(cnt)
        break

    gameover, graph, tail, head = move(graph, head, tail, head_d, tail_d)
    cnt += 1

    if changes:
        if changes[0][0] == cnt:
            change = changes.popleft()
            head_d = rotate(change[1], head_d)
            graph[head[0]][head[1]][1] = head_d