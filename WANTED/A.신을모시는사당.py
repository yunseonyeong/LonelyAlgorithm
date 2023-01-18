import sys
input = sys.stdin.readline

N = input()
rocks = list(map(int, input().strip().split()))

max_cnt = 1
stack = [rocks[0]]

for rock in rocks[1:]:
    if stack[-1] == rock:
        stack.append(rock)

    else:
        if max_cnt < len(stack):
            max_cnt = len(stack)
        stack = [rock]

    if max_cnt < len(stack):
        max_cnt = len(stack)

print(max_cnt)