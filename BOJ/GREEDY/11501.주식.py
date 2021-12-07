# 진짜 죽고 싶은 문제다. 별 거 아닌 문젠데 너무 어렵게 생각했다. 세 코드 모두 답은 잘 나옴
# 첫번째 시도 => 최고가가 아니면 hold 하고, 최고가인 날에는 hold 해놓았던 주식을 모두 판다. 그리고 최고가는 갱신된다. 
# import sys

# T = int(sys.stdin.readline())
# def sell(days, i, hprice) :
#   profit = 0
#   for j in range(hold) :
#     profit += hprice - days[i-j-1]
    
#   return profit

# for _ in range(T) :
#   profit = 0
#   hold = 0
#   N = int(sys.stdin.readline())
#   days = list(map(int, sys.stdin.readline().split()))

#   for i in range(N) :
#     hprice = max(days[i:])
#     if days[i] == hprice :
#       if hold > 0 :
#         profit += sell(days, i, hprice)
#         hold = 0
#     else :
#       hold += 1        # buy

#   print(profit)



# 두번째 시도 => hold 하는 주식을 굳이 기록할 필요 없이 날마다 최고가와의 차이를 수익으로 더해주면 되어서 수정.
# import sys

# T = int(sys.stdin.readline())

# for _ in range(T) :
#   profit = 0
  
#   N = int(sys.stdin.readline())

#   days = list(map(int, sys.stdin.readline().split()))

#   for i in range(N) :
#     hprice = max(days[i:])
#     if days[i] != hprice :
#        profit += hprice - days[i]           # buy

#   print(profit)

# 마지막 시도 => 앞의 두 케이스에서 시간 초과가 발생하는 이유는 매번 최고가를 max()로 계산해야 했기 때문인 것 같다.
# 그래서 최고가를 한번에 계산하지 않고, 주가 리스트를 뒤집어서 최고가보다 [i]가 더 비싸면, 최고가는 갱신하고
# 뒤집은 리스트에서 현재 최고가는 미래의 주가니까 [i]가 최고가보다 싸면, 그 차이는 곧 수익이 된다. 
import sys

T = int(sys.stdin.readline())

for _ in range(T) :
  profit = 0
  
  N = int(sys.stdin.readline())

  days = list(map(int, sys.stdin.readline().split()))
  days.reverse()
  hprice = days[0]

  for i in range(1,N) :
    if days[i] > hprice :
      hprice = days[i]
    else :
      profit += hprice - days[i]

  print(profit)