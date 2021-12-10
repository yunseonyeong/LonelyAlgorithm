import sys

N = int(sys.stdin.readline())
rope = []
for _ in range(N) :
  rope.append(int(sys.stdin.readline()))

rope.sort()
max_weight = rope[0] * N
for i,r in zip(range(1,N), rope[1:]) :
  if r * (N-i) > max_weight :
    max_weight = r * (N-i)

print(max_weight)
