def DFS(airport, path, tickets, visited):
    global answer
    if len(path) == len(tickets) + 1:
        answer.append(path)
        return

    for i, ticket in enumerate(tickets):
        if airport == ticket[0] and not visited[i]:
            visited[i] = True
            DFS(ticket[1], path+[ticket[1]], tickets, visited)
            visited[i] = False

answer = []
def solution(tickets):
    visited = [False for _ in range(len(tickets))]
    global answer
    
    DFS("ICN", ["ICN"], tickets, visited)
    answer.sort(reverse=True)
    return answer[-1]

    