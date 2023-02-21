from collections import deque

def solution(priorities, location):
    queue = deque()
    result = []
    for i, p in enumerate(priorities):
        queue.append((i,p))
    
    while queue:
        j = queue.popleft()
        if j[1] == max(priorities):
            result.append(j)
            priorities.remove(j[1])
            if j[0] == location:
                return len(result)
        else:
            queue.append(j)