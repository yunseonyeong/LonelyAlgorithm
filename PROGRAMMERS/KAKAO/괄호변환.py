def is_balanced(p):
    cnt = 0
    for i in range(len(p)) :
        if p[i] == '(':
            cnt -= 1
        if p[i] == ')':
            cnt += 1
        if cnt == 0:
            return i
        
def is_right(p):
    arr = []
    for i in p :
        if i == '(' :
            arr.append(i)
        else :
            try :
                arr.pop()
            except :
                return False
    
    if len(arr) == 0 :
        return True
    else :
        return False
                
            
def solution(p):
    
    if p == "":
        return 
    u, v = p[:is_balanced(p)+1], p[is_balanced(p)+1:]
    
    if is_right(u):
        answer = u + solution(v)
        return answer
    else :
        answer = '(' + solution(v) + ')'
        tr = str.maketrans('()',')(')
        answer += u[1:-1].translate(tr)
        return answer

        