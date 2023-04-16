def dfs(idx, computers, visited):
    visited[idx] = True
    for i,neigh in enumerate(computers[idx]):
        if not visited[i] and computers[idx][i] == 1:
            dfs(i, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
    
    return answer