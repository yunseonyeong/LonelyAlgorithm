# 기둥 설치 가능 : (y == 0) or (x,y-1 == 기둥) or (x-1, y == 보) or (x,y == 보)
# 보 설치 가능 : x,y-1 == 기둥 or x+1,y-1 == 기둥 or (x-1, y == 보 and x+1, y == 보) 
def check(field):
    for x,y,what in field:
        if what == 0:
            # 기둥
            if y != 0 and [x,y-1,0] not in field and [x-1,y,1] not in field and [x,y,1] not in field:
                return False
                
        else:
            if [x,y-1,0] not in field and [x+1,y-1,0] not in field and ([x-1,y,1] not in field or [x+1,y,1] not in field):
                return False
    return True
                

def solution(n, build_frame):
    field = []
    for x,y,what,how in build_frame:
        if how == 0:
            field.remove([x,y,what])
            if not check(field):
                field.append([x,y,what])
        else:
            field.append([x,y,what])
            if not check(field):
                field.remove([x,y,what])
                
    return sorted(field)