import time

def binary(n):
    memo[1] = 1
    memo[2] = 2
    if n in list(memo.keys()):
        return memo[n]
    else:
        binary(n-1)
        memo[n]  = (memo[n-1] + memo[n-2]) % 15746
        return memo[n]
n = int(input())

memo = {}
start_time = time.time()
print(binary(n))
print(time.time() - start_time)


'''
n = 1
1

n = 2
00
11

n = 3
001
100
111

n = 4
0000
0011
1001
1100
1111

n = 5
00001
00100
10000
00111
10011
11001
11100
11111
'''