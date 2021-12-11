import sys

N = int(sys.stdin.readline())
nums = []
cnt = 9
ans = 0

for _ in range(N): 
  nums.append(sys.stdin.readline().rstrip())

numList = dict()

for num in nums :
  n_len = len(num)
  for n in num :
    if n in numList:
      numList[n] += 10**(n_len-1)
    else :
      numList[n] = 10**(n_len-1)
    n_len -= 1

# A:10000, C:1000 D:100 E:10 B:1
# G:100, C:1010, F:1

alphaList = sorted(list(numList.values()), reverse=True)

for alpha in alphaList :
  ans += alpha * cnt
  cnt -= 1

print(ans)