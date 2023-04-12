import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    numbers = []
    n = int(input())
    for _ in range(n):
        numbers.append(input().strip())

    numbers.sort()
    answer = True

    for i in range(len(numbers)-1):
        if numbers[i][:len(numbers[i])] == numbers[i+1][:len(numbers[i])]:
            print("NO")
            answer = False
            break
        
    if answer :
        print("YES")