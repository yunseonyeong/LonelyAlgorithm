from collections import deque

def create_map(x,y,n, board, visited, maps, typed):
    if typed == 't':
        c = 1
    else:
        c = 0
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = True
    holes = [[x,y]]
    while queue:
        now = queue.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == c:
                visited[nx][ny] = True
                queue.append((nx, ny))
                holes.append([nx, ny])
    
    holesX = sorted(holes, key=lambda x: x[0])
    holesY = sorted(holes, key=lambda x: x[1])
    N = holesX[-1][0] - holesX[0][0] + 1
    M = holesY[-1][1] - holesY[0][1] + 1
    offsetX = holesX[0][0]
    offsetY = holesY[0][1]
    holes_map = []
    
    for sx,sy in holes:
        sx-=offsetX
        sy-=offsetY
        holes_map.append((sx,sy))
    

    maps.append([N,M, holes_map])

    return visited, maps

def make_block(N,M,holes_map):
    result = [[0] * M for _ in range(N)]
    for i,j in holes_map:
        result[i][j] = 1
    return (result,len(holes_map))

def rotate(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

def compare(arrA, arrB):
    if len(arrA) != len(arrB) or len(arrA[0]) != len(arrB[0]):
        return False
    else:
        N = len(arrA)
        M = len(arrA[0])
        for i in range(N):
            for j in range(M):
                if arrA[i][j] != arrB[i][j]:
                    return False
        return True
    
answer = 0
def solution(game_board, table):
    global answer
    n = len(game_board)
    visitedB = [[False for _ in range(n)] for _ in range(n)]
    visitedT = [[False for _ in range(n)] for _ in range(n)]

    board_map = []
    table_map = []
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visitedB[i][j]:
                visitedB,board_map = create_map(i,j,n,game_board, visitedB, board_map, 'b')
                
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visitedT[i][j]:
                visitedT, table_map = create_map(i,j,n,table, visitedT, table_map, 't')
    

    block_b = []
    block_t = []

    for N,M,holes in board_map:
        block_b.append(make_block(N,M,holes))
    
    for N,M,holes in table_map:
        block_t.append(make_block(N,M,holes))

    for t,lt in block_t:
        matched = False
        for b,lb in block_b:
            if (len(b) == len(t) and len(b[0]) == len(t[0])) or (len(b) == len(t[0]) and len(t) == len(b[0])):
                for _ in range(4):
                    if compare(t, b):
                        block_b.remove((b,lb))
                        matched = True
                        answer += lt
                        break
                    t = rotate(t)
            if matched:
                break
    
    return answer