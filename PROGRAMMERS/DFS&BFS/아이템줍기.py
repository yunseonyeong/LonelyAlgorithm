from collections import deque

def BFS(x,y, itemX, itemY, graph):
    visited = [[0 for _ in range(102)] for _ in range(102)]
    queue = deque()
    queue.append((x,y))
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    while queue:
        now = queue.popleft()
        if now[0] == itemX and now[1] == itemY:
            break
        for i in range(4):
            nx = dx[i] + now[0]
            ny = dy[i] + now[1]
            if 0<nx<102 and 0<ny<102 and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[now[0]][now[1]] + 1
    return visited[itemX][itemY]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    for r in rectangle:
        [x1, y1, x2, y2] = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1
                    
    return(BFS(characterX*2, characterY*2, itemX*2, itemY*2, graph)//2)