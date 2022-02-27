str1 = input().strip()
str2 = input().strip()
N = len(str1)
M = len(str2)
LCS = [[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,M+1):
    if str1[i-1] == str2[j-1]:
      LCS[i][j] = LCS[i-1][j-1] + 1
    else :
      LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[N][M])