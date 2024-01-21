import sys
input = sys.stdin.readline
from collections import deque

S,P = map(int, input().split())
D = input().strip()
[gA, gC, gG, gT] = list(map(int, input().split()))
subStr = deque()
ans = 0

def check(arr):
    [nA, nC, nG, nT] = [0,0,0,0]
    for a in arr:
        if a == 'A':
            nA += 1
        elif a == 'C':
            nC += 1
        elif a == 'G':
            nG += 1
        elif a == 'T':
            nT += 1
    
    return nA, nC, nG, nT


for d in D[0:P]:
    subStr.append(d)

nA,nC,nG,nT = check(subStr)
if nA >= gA and nC >= gC and nT >= gT and nG >= gG:
    ans += 1

for i in range(S-P):
    if subStr[0] == 'A':
        nA -= 1
    elif subStr[0] == 'C':
        nC -= 1
    elif subStr[0] == 'G':
        nG -= 1
    elif subStr[0] == 'T':
        nT -= 1  
    
    subStr.popleft()

    if D[i+P] == 'A':
        nA += 1
    elif D[i+P] == 'C':
        nC += 1
    elif D[i+P] == 'G':
        nG += 1
    elif D[i+P] == 'T':
        nT += 1
    
    subStr.append(D[i+P])
    print(subStr)

    if nA >= gA and nC >= gC and nT >= gT and nG >= gG:
        ans += 1

print(ans)