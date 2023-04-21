import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(n):
    global cnt
    if not visited[n]:
        visited[n] = True
        cnt += 1
        order[n] = cnt
        if n in graph.keys():
            for neighbor in graph[n]:
                DFS(neighbor)

N,M,R = map(int, input().split())
graph = {}
visited = [False for _ in range(N+1)]
order = [0 for _ in range(N+1)]
cnt = 0

for _ in range(M):
    u,v = map(int, input().split())
    if u in graph.keys():
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph.keys():
        graph[v].append(u)
    else:
        graph[v] = [u]

for g in graph.values():
    g.sort()

DFS(R)

for v in range(1, N+1):
    print(order[v])