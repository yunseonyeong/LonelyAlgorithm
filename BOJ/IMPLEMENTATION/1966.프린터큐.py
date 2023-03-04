import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    priority = []
    priority = deque(map(int, input().split()))
    idx = deque(list(range(N)))
    cnt = 0

    while priority:
        m = max(priority)
        p = priority.popleft()
        i = idx.popleft()    
        
        if p == m:
            cnt += 1
            if i == M:
                break

        else:
            priority.append(p)
            idx.append(i)

    print(cnt)
