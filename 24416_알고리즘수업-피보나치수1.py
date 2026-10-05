memo = []

def fib(n):
    if n == 1 or n == 2:
        memo.append(1)
    elif n > 2:
        memo.append(memo[n-1] + memo[n-2])
        return memo[n]

T = 10 # int(input())
count = 0
for t in range(1, T+1):
    count += 1
    print(t, fib(t), count)
    