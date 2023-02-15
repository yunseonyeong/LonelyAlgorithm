def solution(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    
    return len(stack) == 0