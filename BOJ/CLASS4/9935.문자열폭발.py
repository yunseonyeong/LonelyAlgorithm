strr = input()
bomb = input()
lenbomb = len(bomb)

stack = []

for s in strr :
  stack.append(s)
  if len(stack) >= len(bomb):
    if stack[-lenbomb:] == list(bomb) :
      for _ in range(lenbomb):
        stack.pop()
  
if not stack:
  print("FRULA")
else:
  print("".join(stack))
