import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N+1)]
parent = [0] * (N+1)
visited = [False]*(N+1)

for _ in range(1,N):
  n1,n2 = map(int, input().split())
  tree[n1].append(n2)
  tree[n2].append(n1)

def dfs(n):
  visited[n] = True
  for val in tree[n]:
    if not visited[val]:
      visited[val] = True
      parent[val] = n
      dfs(val)

dfs(1)
for p in parent[2:] :
  print(p)