def Hanoi_Tower(N, start, end, middle):
    if N == 1:
        print(start, end)
    else:
        Hanoi_Tower(N-1, start, middle, end) # 1번 기둥의 n-1 개의 원반을 2번 기둥으로 옮긴다
        print(start, end) 
        Hanoi_Tower(N-1, middle, end, start) # 2번 기둥의 n-1개의 원반을 3번 기둥으로 옮긴다

n = int(input())
print(2**n - 1)
Hanoi_Tower(n, 1,3,2)