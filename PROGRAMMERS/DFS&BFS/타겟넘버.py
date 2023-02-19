def dfs(numbers, target, answer, cnt):
    global result
    if cnt == len(numbers):
        if answer == target:
            result += 1
        return result
                
    else :
        dfs(numbers, target, answer + numbers[cnt], cnt+1)
        numbers[cnt] *= -1 
        dfs(numbers, target, answer + numbers[cnt], cnt+1)

def solution(numbers, target):
    global result
    result = 0
    dfs(numbers, target, 0, 0)
    return result