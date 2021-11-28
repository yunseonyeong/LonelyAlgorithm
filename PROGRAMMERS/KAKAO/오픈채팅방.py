def solution(record):
    result = []
    name = {}
    
    for r in record :
        s = r.split()
        
        if s[0] == "Enter" or s[0] == "Change":
            name[s[1]] = s[2]
    
    for r in record :
        s = r.split()
        if s[0] == "Enter":
            result.append(name[s[1]] + '님이 들어왔습니다.')
        elif s[0] == "Leave":
            result.append(name[s[1]] + '님이 나갔습니다.')

    return result