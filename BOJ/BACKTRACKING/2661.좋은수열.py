import sys
N = int(input())
numbers = ['1','2','3']
result = ''

def check(result,n):
    for i in range(1, (n+1)//2+1):
        if result[-i:] == result[-2*i:-i]:
            return False
    return True

def backtracking(n):
    global result
    if n == N:
        print(result)
        exit(0)

    else:
        for number in numbers:
            result += number
            if check(result, n):
                backtracking(n+1)
            result=result[:-1]

backtracking(0)