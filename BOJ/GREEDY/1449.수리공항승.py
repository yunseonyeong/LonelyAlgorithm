# ㅎㅎ 15분 컷 
# 첫 테이프 끝점이 다음 테이프 + 0.5 보다 크면, 테이프 추가 필요 없음
# 그렇지 않으면, 테이프 추가 및 시작점 및 끝점 업데이트

import sys

N, L = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))

leak.sort()
endpoint = leak[0] - 0.5 + L
cnt = 1

for i in range(1,N) :
  if endpoint < leak[i] + 0.5 :
    cnt += 1
    startpoint = leak[i]-0.5
    endpoint = startpoint + L

print(cnt)





