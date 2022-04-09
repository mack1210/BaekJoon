class Stack:
    def __init__(self):
        self.lst = []
    
    def push(self, factor):
        self.lst.append(factor)
    
    def pop(self):
        self.lst.pop()
        
    def show(self):
        print(self.lst)
    
        

N = int(input())

for i in range(N):
    lst = Stack()
    vps = input()
    for j in vps:
        if j == '(':
            lst.push(j)
        elif j == ')':
            if len(lst.lst):
                if lst.lst[-1] == '(':
                    lst.pop()
                else:
                    lst.push(j)
            else:
                lst.push(j)
                
            
    if len(lst.lst):
        print("NO")
    else:
        print("YES")
    
    