# 더하기를 먼저 다 해준다음에, 빼기를 해줘야 큰 수를 빼어 결과값이 작아질 수 있다. 

S = input().split('-')
plus_result = []    # 부분 덧셈 끝난 값들만 넣을 리스트
# S = ['55', '50+40']

for s in S :
  value = 0     # 플러스 연산값 저장할 변수
  plus = s.split('+')

  for p in plus :
    value += int(p)
  plus_result.append(value)

  # plus_result = [55, 90]

result = plus_result[0]

for r in plus_result[1:] :
  result -= r

print(result)


    
