from itertools import combinations

def solution(orders, course):
    answer = []
    for i in range(len(orders)) :
        orders[i] = sorted(orders[i])
        
    for c in course :
        cnt = dict()
        for o in orders:
            if len(o) >= c:
                result= combinations(o,c)
                for r in result :
                    t = "".join(r)
                    if t in cnt :
                        cnt[t] += 1
                    else :
                        cnt[t] = 1
        
        result=[k for k,v in cnt.items() if max(cnt.values()) == v and v != 1]
        answer+=result

    return sorted(answer)