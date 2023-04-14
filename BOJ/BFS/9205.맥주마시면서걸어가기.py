import sys
inpupt = sys.stdin.readline
from collections import deque

def BFS(x,y):
    global visited, store_list, festival
    queue = deque()
    queue.append((x,y))
    while queue:
        now = queue.popleft()
        if abs(now[0]-festival[0]) + abs(now[1]-festival[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                if abs(now[0]-store_list[i][0]) + abs(now[1]-store_list[i][1]) <= 1000:
                    visited[i] = True
                    queue.append((store_list[i][0], store_list[i][1]))

    print("sad")

t = int(input())

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store_list = []
    for _ in range(n):
        store_list.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [False for _ in range(n)]
    BFS(home[0], home[1])


                