from collections import deque

def BFS(x, n, graph):
    queue = deque()
    queue.append(x)
    cnt = 1
    visited = [False for _ in range(n+1)]
    visited[x] = True
    
    while queue:
        now = queue.popleft()
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True
                cnt += 1
                queue.append(n)
                
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        [s,e] = wire
        graph[s].append(e)
        graph[e].append(s)
    
    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
        cnta = BFS(a, n, graph)
        graph[a].append(b)
        graph[b].append(a)
        cntb = n - cnta
        if answer > abs(cntb-cnta):
            answer = abs(cntb-cnta)
    
    return answer
        
        