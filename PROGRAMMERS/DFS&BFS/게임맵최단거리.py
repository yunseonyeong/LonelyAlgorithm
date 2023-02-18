from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = True
    direction = [(1,0), (-1,0), (0,-1), (0,1)] # 상, 하, 좌, 우

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny] :
                queue.append((nx,ny))
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
        
    
    if maps[n-1][m-1] > 1 :
        return maps[n-1][m-1]
    else:
        return -1