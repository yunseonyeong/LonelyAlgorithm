import sys
input = sys.stdin.readline
from collections import deque

S = input().rstrip()
M = int(input())
cursor = len(S)
before = deque(list(S))
after = deque([])

for _ in range(M):
    l = input().strip()
    if l[0] == 'P':
        op = l[0]
        n = l.split()[1]
        before.append(n)

    elif l[0] == 'D':
        if len(after) > 0:
            a = after.popleft()
            before.append(a)

    elif l[0] == 'B':
        if len(before) > 0:
            before.pop()

    elif l[0] == 'L':
        if len(before) > 0:
            b = before.pop()
            after.insert(0, b)

print("".join(before) + "".join(after))