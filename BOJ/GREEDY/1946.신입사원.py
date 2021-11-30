import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :     # test case 수만큼 반복
    N = int(sys.stdin.readline().rstrip())
    score_list = [0]*N
    result = 1
  
    for _ in range(N):      # 지원자 수만큼 반복
        score = list(map(int, sys.stdin.readline().rstrip().split(" ")))     # 서류성적, 면접성적 list 
        score_list[score[0]-1] = score             # 이차원 배열로 전 지원자 성적 모두 list
  
    rank = score_list[0][1]     # 면접 점수 랭크 기록

    for i in range(N) :
        if score_list[i][1] < rank :
            rank = score_list[i][1]       # 리스트에 다 넣어놓고 나중에 sort 하는것보다, 넣으면서 인덱스로 바로바로 정렬하는것이 더 깔끔해서 수정.
            result += 1
      
    print(result)
      

