import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    execution = input().strip()
    n = int(input())
    reverse_cnt = 0
    arr_str = input().strip()
    arr = deque(arr_str[1:-1].split(','))
    err = False
    if n == 0:
        arr = deque()

    for e in execution:
        if e == "R":
            reverse_cnt += 1
        elif e == "D":
            if len(arr) == 0:
                print("error")
                err = True
                break
            else:
                if reverse_cnt % 2 == 1:
                    arr.pop()
                else:
                    arr.popleft()
    
    if err:
        continue
    if reverse_cnt % 2 == 1:
        arr.reverse()
    print('[' + ','.join(arr) + ']')