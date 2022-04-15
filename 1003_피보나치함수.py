def fibo(n):
    global memo
    memo = {0: [1, 0], 1: [0, 1]}
    if n == 0:
        return memo[n]
    if n == 1:
        return memo[n]
    if n>1:
        # memo를 n-1까지 만들어준다.
        fibo(n-1)
        # memo n번째 값을 넣어준다.
        memo[n] = [sum(x) for x in zip(memo[n-1], memo[n-2])]
    return memo[n]

N = int(input())
for i in range(N):
    k = int(input())
    answer = fibo(k)
    print(answer[0], answer[1])
