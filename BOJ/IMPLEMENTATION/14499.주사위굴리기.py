import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

move_map = list(map(int, input().split()))

bottom, top, right, left, front, back = 0,0,0,0,0,0

dice = [bottom, top, right, left, front, back]

def move_dice(dice, d):
    if d == 1:
        btm,t = dice[2],dice[3]
        r,l = dice[1],dice[0]

        dice[0],dice[1] = btm,t
        dice[2],dice[3] = r,l

    elif d == 2:
        btm,t = dice[3],dice[2]
        r,l = dice[0],dice[1]

        dice[0],dice[1] = btm,t
        dice[2],dice[3] = r,l
    
    elif d == 3:
        btm,t = dice[5],dice[4]
        f,bck = dice[0],dice[1]

        dice[0],dice[1] = btm,t
        dice[4],dice[5] = f,bck
    
    elif d == 4:
        btm,t = dice[4],dice[5]
        f,bck = dice[1],dice[0]

        dice[0],dice[1] = btm,t
        dice[4],dice[5] = f,bck

    return dice

def copy_num(bottom, nx, ny, graph):
    if graph[nx][ny] == 0:
        graph[nx][ny] = bottom
    else:
        bottom = graph[nx][ny]
        graph[nx][ny] = 0

    return graph, bottom

direction = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]
for move in move_map:
    nx = x + direction[move][0]
    ny = y + direction[move][1]

    if 0<=nx<N and 0<=ny<M :
        dice = move_dice(dice, move)
        graph, bottom = copy_num(dice[0], nx, ny, graph)
        dice[0] = bottom
        x,y = nx,ny
    
        print(dice[1])