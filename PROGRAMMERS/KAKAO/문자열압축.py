def solution(s):
    n = len(s)
    answer = []
    if n == 1:
        return 1
    for leng in range(1,n//2+1):
        l = ''
        sliced = s[:leng]
        cnt = 1
        for i in range(leng, leng+n, leng):
            if sliced == s[i:i+leng]:
                cnt += 1
            else :
                if cnt == 1:
                    l = l + sliced
                else :
                    l = l + str(cnt) + sliced
                    cnt = 1
            
            sliced = s[i:i+leng]
        answer.append(len(l))
    return min(answer)