import sys
input = sys.stdin.readline

def BackTracking(start, visited, S, B):
    global minBS
    if B != 0:
        minBS = min(minBS, abs(S-B))

    for i in range(start,N):
        if not visited[i]:
            visited[i] = True
            BackTracking(start+1, visited, S*ingredient[i][0], B+ingredient[i][1])
            visited[i] = False

N = int(input())
ingredient = []
minBS = int(1e9)
visited=[False]*N

for _ in range(N):
    ingredient.append(list(map(int, input().split())))

BackTracking(0,visited, 1,0)

print(minBS)