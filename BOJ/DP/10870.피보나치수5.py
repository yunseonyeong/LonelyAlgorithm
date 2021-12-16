N = int(input())
fib = [0 for _ in range(N+1)]

def dp(N) :
  if fib[N] != 0 :
    return fib[N]
  if N == 0 or N == 1:
    return N
  fib[N] = dp(N-1) + dp(N-2)
  return fib[N]

print(dp(N))
