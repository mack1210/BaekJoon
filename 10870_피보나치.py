def FIV(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    elif N >= 2:
        return FIV(N-1) + FIV(N-2)

N = int(input())
print(FIV(N))