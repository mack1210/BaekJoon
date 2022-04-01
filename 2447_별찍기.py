# numpy를 쓰면 백준에서는 런타임에러가 발생한다.
import numpy as np
from time import time

def make_starts(N):
    star = np.zeros((N,N))
    
    pattern = [[1,1,1], [1,0,1], [1,1,1]]
    N_prime = int(N/3)
    
    if N_prime == 1:
        star = pattern
    else:
        for i in range(0, N, N_prime):
            for j in range(0, N, N_prime):
                if i == N_prime and j == N_prime:
                    continue
                else:
                    star[i:i+N_prime, j:j+N_prime] = make_starts(N_prime)
    return star

N = int(input())
start_time = time()

stars= make_starts(N)
for i in range(N):
    for j in range(N):
        if stars[i,j] == 1:
            print("*", end = " ")
        else:
            print(" ", end= " ")
    print()
print(time()-start_time)



# numpy를 쓰면 백준에서는 런타임에러가 발생한다.
# 넘파이 없이 시도할 것
# import numpy as np
from time import time

def make_starts(N):
    star = [[0]*N]*N
    
    pattern = [[1,1,1], [1,0,1], [1,1,1]]
    N_prime = int(N/3)
    
    if N_prime == 1:
        star = pattern
    else:
        for i in range(0, N, N_prime):
            for j in range(0, N, N_prime):
                if i == N_prime and j == N_prime:
                    continue
                else:
                    star = make_starts(N_prime)
                    star[int(i%3)][int(j%3)] = star[i:i+N_prime][j:j+N_prime]
    return star

N = 9# int(input())
start_time = time()

stars= make_starts(N)
for i in range(N):
    for j in range(N):
        if stars[i][j] == 1:
            print("*", end = " ")
        else:
            print(" ", end= " ")
    print()
print(time()-start_time)