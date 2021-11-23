def factorial(N):
    if N == 0:
        return 1
    else:
        N * factorial(N-1)

N = input()
print(factorial(N))
