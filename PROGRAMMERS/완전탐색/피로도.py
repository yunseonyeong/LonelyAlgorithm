answer = 0
visited = []

def dfs(k, count, dungeons):
    global answer
    if count > answer:
        answer = count

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = True
            dfs(k-dungeons[i][1], count+1, dungeons)
            visited[i] = False

def solution(k, dungeons):
    global visited
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons)
    return answer
