def solution(brown, yellow):
    S = brown + yellow
    h = 3
    w = 3
    while True:            
        if S%h != 0:
            h+=1
            continue
        w = S/h
        if w*h - (w-2)*(h-2) == brown:
            return [w,h]
        h+=1