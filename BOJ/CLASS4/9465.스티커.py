import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  graph = []
  N = int(input())
  for _ in range(2):
    graph.append(list(map(int, input().split())))
  for i in range(1,N):
    if i == 1:
      graph[0][1] += graph[1][0]
      graph[1][1] += graph[0][0]

    else:
      graph[0][i] = max(graph[1][i-2], graph[1][i-1]) + graph[0][i]
      graph[1][i] = max(graph[0][i-2], graph[0][i-1]) + graph[1][i]
      
  print(max(graph[0][N-1], graph[1][N-1]))