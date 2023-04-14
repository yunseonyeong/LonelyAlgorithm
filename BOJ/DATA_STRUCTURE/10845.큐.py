import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque([])

for _ in range(N):
    op = input().strip()

    if 'push' in op:
        n = int(op.split()[1])
        queue.append(n)

    elif op == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif op == 'size':
        print(len(queue))

    elif op == 'empty':
        if len(queue) == 0:
            print(1)
        else: 
            print(0)

    elif op == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif op == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

