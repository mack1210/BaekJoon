

def pattern(N):
    for i in range(N):
        if i%3 == 1:
            print("* *"*int(N/3))
        else:
            print("***"*int(N/3))
            
   

def make_stars(N):
    import math
    k = int(math.log(N, 3))
    if N == 3:
        pattern(N)
    else:
        pattern(N)


N = 27 # int(input()
make_stars(N) 