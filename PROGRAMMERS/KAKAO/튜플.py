def solution(s):
    s = s.replace('{{', '').replace('}}','')
    a = s.split('},{')
    result = ['str' for i in range(len(a))]
    answer = []

    for t in a :
        c = t.count(',')
        result[c] = t
    
    for r in result :
        r_split = r.split(',')
        for rs in r_split :
            if int(rs) not in answer :
                answer.append(int(rs))        
    
    return answer