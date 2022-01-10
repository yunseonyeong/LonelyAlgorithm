import sys
input = sys.stdin.readline

bar = list(input().strip())
answer = 0
stack = []

for i in range(len(bar)):
  if bar[i] == '(':
    stack.append('(')
  else :
    if bar[i-1] == '(':
      stack.pop()
      answer += len(stack)
    else :
      stack.pop()
      answer += 1

print(answer)

