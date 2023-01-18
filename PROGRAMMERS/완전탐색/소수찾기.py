import math
import itertools

def is_prime(number):
    n = int(number)
    if n <= 1:
        return False
    p = math.floor(math.sqrt(n))
    
    for i in range(2, p+1):
        if n % i == 0:
            return False
    
    return True
    

def solution(numbers):
    permu = []
    answer = []
    for i in range(1, len(numbers)+1):
        permu += list(map(''.join, itertools.permutations(numbers, i)))

    for p in permu:
        if is_prime(p):
            answer.append(int(p))

    answer = set(answer)
    answer = list(answer)
    return len(answer)

