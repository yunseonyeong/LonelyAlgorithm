while True :
    S = input()
    stack = []

    if S == "." :
        break

    for s in S :
        if s == '[' or s == '(' :
            stack.append(s)
        elif s == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                stack.append(']')
                break
        elif s == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')