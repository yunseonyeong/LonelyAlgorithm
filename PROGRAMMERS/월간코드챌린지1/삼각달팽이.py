def solution(n):
    answer = []
    graph = [[0] * n for _ in range(n)]
    row  = -1
    col = 0
    num = 1
    for i in range(n,0,-3):
        for j in range(i):
            row += 1
            graph[row][col] = num
            num += 1
        for j in range(i-1):
            col += 1
            graph[row][col] = num
            num += 1
        for j in range(i-2):
            row -= 1
            col -= 1
            graph[row][col] = num
            num += 1
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                answer.append(graph[i][j])

    return answer

