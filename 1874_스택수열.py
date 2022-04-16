class Stack:
    def __init__(self):
        self.lst = [] 
    
    def push(self, x):
        self.lst.append(x)
        print('+')
    
    def pop(self):
        print('-')
        return self.lst.pop()
    
    def last(self):
        if len(self.lst):
            return self.lst[-1]
        else:
            return 0
        
    def all_list(self):
        return self.lst
        
    def show(self):
        print(self.lst)

N = 8
arr = []
S = Stack()

last_pop = 0
cnt = 0
max = 0
for i in range(N):
    num = int(input())
    
    # 매번 최댓값을 갱신해 준다
    if num > max:
        max_new = num
        
        # 최댓값이 갱신되면 cnt를 0으로 설정
        cnt = 0
    print(max, max_new)
    # cnt가 0이 아니면
    if cnt:
        if S.all_list().index(num):
            front = S.all_list().index(num)
            end = S.last()
            
            for k in range(front, end):
                print('index {0}, last {1}'.format(front,end))
                S.pop()
    # cnt가 0이면
    else:
        # 이전 최댓값에서 부터 새로 받은 값까지 push 
        for j in range(max+1, max_new+1):
            max = max_new
            S.push(j)
        
        # 스택의 마지막 값이 j와 같아지면 pop
        if S.last() == j:
            S.pop()
        cnt += 1
    
    S.show()