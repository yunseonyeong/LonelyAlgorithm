import sys
input = sys.stdin.readline

def check(wheels, num, direction):
    visited = [False for _ in range(5)]
    visited[num] = True
    stack = [(direction, num)]
    result = [(direction, num)]
    while stack:
        d, s = stack.pop()

        if s - 1 > 0 and not visited[s-1]:
            if wheels[s][-2] != wheels[s-1][2]:
                visited[s-1] = True
                stack.append((-1*d, s-1))
                result.append((-1*d, s-1))
        
        if s + 1 <= 4 and not visited[s+1]:
            if wheels[s][2] != wheels[s+1][-2]:
                visited[s+1] = True
                stack.append((-1*d, s+1))
                result.append((-1*d, s+1))
    
    return result
        

def rotate(wheels, result):
    tmp = ["" for _ in range(5)]

    for i in range(1,5):
        tmp[i] = wheels[i]

    for direction, num in result:
        if direction == -1:
            tmp[num] = wheels[num][1:] + wheels[num][0]
        elif direction == 1:
            tmp[num] = wheels[num][-1] + wheels[num][:-1]

    return tmp



wheels = [""]
answer = 0

for _ in range(4):
    wheels.append(input().rstrip())

T = int(input())
for _ in range(T):
    num, direction = map(int, input().split())
    result = check(wheels, num, direction)
    wheels = rotate(wheels, result)

for i in range(1,5):
    answer += int(wheels[i][0]) * (2**(i-1))

print(answer)