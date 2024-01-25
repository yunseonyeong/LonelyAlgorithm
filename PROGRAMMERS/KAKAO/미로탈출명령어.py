import sys
sys.setrecursionlimit(10**8)

def getDist(x,y,r,c):
    return abs(x-r) + abs(y-c)
    
def dfs(x,y,n,m,r,c,way,cnt,k):
    global answer
    d = [(1,0), (0,-1), (0,1), (-1,0)]
    w = ['d', 'l', 'r', 'u']
    
    if x<=0 or x>n or y<=0 or y>m:
        return
    if k < cnt + getDist(x,y,r,c):
        return
    if x == r and y == c and cnt == k:
        answer = way
        return 
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 < nx <= n and 0 < ny <= m and way < answer:
            dfs(nx,ny,n,m,r,c,way+w[i],cnt+1,k)
            
answer = 'z'
def solution(n, m, x, y, r, c, k):
    global answer
    if getDist(x,y,r,c) > k or (k-getDist(x,y,r,c)) % 2 == 1:
        return 'impossible'
    dfs(x,y,n,m,r,c,"",0,k)

    return answer