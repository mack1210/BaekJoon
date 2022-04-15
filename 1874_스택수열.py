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
        
    def show(self):
        print(self.lst)

N = 8
arr = []
S = Stack()

last_pop = 0

for i in range(N):
    num = int(input())
    
    if S.last() <= num:
        for j in range(last_pop+1,num+1):
            S.push(j)
            
    pop_val_pred = S.last()
    if last_pop < pop_val_pred:
        last_pop = S.pop()
    if num == pop_val_pred:
        S.pop()
    
    
    
    
    S.show()