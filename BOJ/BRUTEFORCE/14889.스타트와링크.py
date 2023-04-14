import sys
input = sys.stdin.readline
from itertools import combinations
from copy import deepcopy

graph = []
com = []
N = int(input())
result = 1e9
for i in range(1,N+1):
    com.append(i)

combination = combinations(com, N//2)

for _ in range(N):
    graph.append(list(map(int, input().split())))

for combi in combination:
    start_power = 0
    link_power = 0
    start_pairs = combinations(combi, 2)
    for pair in start_pairs:
        start_power += graph[pair[0]-1][pair[1]-1] + graph[pair[1]-1][pair[0]-1]
    
    link = deepcopy(com)
    for c in combi:
        link.remove(c)

    link_pairs = combinations(link, 2)
    for pair in link_pairs:
        link_power += graph[pair[0]-1][pair[1]-1] + graph[pair[1]-1][pair[0]-1]
    
    result = min(result, abs(start_power - link_power))
    print(result)