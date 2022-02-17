import sys
input = sys.stdin.readline

N,M = map(int, input().split())
visited = [False]*(N)
result = []

def permutation(N,M,level,idx):
	if level == M :
		print(' '.join(map(str, result)))
		return
	for i in range(idx,N):
		if visited[i] == False:
			visited[i] = True
			result.append(i+1)
			permutation(N,M,level+1,i+1)
			visited[i] = False
			result.pop()

permutation(N,M,0,0)