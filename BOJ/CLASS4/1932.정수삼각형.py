import sys
input = sys.stdin.readline

N = int(input())
tree = []
for _ in range(N):
  tree.append(list(map(int, input().split())))

# [level][n] => [level+1][n], [level+1][n+1] 탐색 가능
def dp():
  level = 2
  for i in range(1,N):
    for j in range(level):
      if j == 0:
        tree[i][j] = tree[i][j] + tree[i-1][j]
      elif j == i:
        tree[i][j] = tree[i][j] + tree[i-1][j-1]
      else:
        tree[i][j] = max(tree[i-1][j-1], tree[i-1][j]) + tree[i][j]
    level += 1

dp()
print(max(tree[N-1]))