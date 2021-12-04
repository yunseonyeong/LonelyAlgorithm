import sys
N,M = map(int,input().split())       # row, column
A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0

def convertA(i,j) :          # 부분 배열 A[i][j] 기준으로 뒤집는 함수
  for x in range(i, i+3) :
    for y in range(j, j+3) :
      if A[x][y] == 0 :
        A[x][y] = 1
      else :
        A[x][y] = 0

for i in range(N) :       # Before리스트
  tmp = sys.stdin.readline()
  for j in range(M) :
    A[i][j] = int(tmp[j])

for i in range(N) :     # After리스트
  tmp = sys.stdin.readline()
  for j in range(M) :
    B[i][j] = int(tmp[j])


for i in range(N-2) :
  for j in range(M-2) :
    if A[i][j] != B[i][j] :
      convertA(i,j)
      cnt += 1

for i in range(N) :
  for j in range(M) :
    if A[i][j] != B[i][j] :
      cnt = -1

print(cnt)






  


