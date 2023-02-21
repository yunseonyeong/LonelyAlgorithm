def solution(citations):
    n = len(citations)
    max_h = 0
    
    for h in range(1, n+1):
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1
        if cnt >= h:
            max_h = h
            
    return max_h