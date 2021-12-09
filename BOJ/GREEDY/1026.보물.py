# 헤 헤 5분 컷 .. 실버 3 4 조 아 조 아 
# A를 재배열 하고, B는 재배열 하지 않는다는게, 말만 그렇다는 거지 
# 그냥 A의 가장 작은 수 X B의 가장 큰 수 이렇게 곱하면 결과값이 가장 작을 것이다. 

# A는 오름차순으로, B는 내림차순으로 정렬하여 같은 인덱스끼리 묶어준다. 

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)


result = 0
for i in range(N) :
  result += A[i] * B[i]

print(result)


