import sys
input = sys.stdin.readline

def backtracking(start, password):
    vo = 0
    co = 0
    if len(password) == L:
        for p in password:
            if p in vowels:
                vo += 1
            else:
                co += 1
        if vo >= 1 and co >= 2 :
            print("".join(password))

        return

    for i in range(start, C):
        password += arr[i]
        backtracking(i+1, password)
        password = password[:-1]


L,C = map(int, input().split())
arr = list(input().split())
arr.sort()
vowels = ['a','e','i','o','u']
password = ''

backtracking(0, password)