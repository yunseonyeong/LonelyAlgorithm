import sys
input = sys.stdin.readline
import heapq

n = int(input())
q1 = [] 
q2 = [] 

for i in range(n):
    a = int(input())
    if a < 0:
        heapq.heappush(q1, -a) 
    elif a > 0:
        heapq.heappush(q2, a) 
    else:
        if len(q1) == 0 :
            if len(q2) == 0 :
                print(0)
            else:
                print(heapq.heappop(q2))
        elif len(q2) == 0 :
            print(-heapq.heappop(q1))

        else :
            n1 = -q1[0]
            n2 = q2[0]

            if abs(n1) > abs(n2) :
                print(n2)
                heapq.heappop(q2)

            else:
                print(n1)
                heapq.heappop(q1)