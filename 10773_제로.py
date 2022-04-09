import sys
class Stack:
    def __init__(self) -> None:
        self.lst = []
        
    def push(self, X):
        self.lst.append(X)
    
    # pop에 대한 알고리즘을 알고 싶지만 방법을 찾지 못함
    def pop(self):
        self.lst.pop()
        
    def sum(self):
        return sum(self.lst)
        

N = int(sys.stdin.readline())
lst = Stack()


for i in range(N):
    order = int(sys.stdin.readline())
    if order != 0:
        lst.push(order)
    else:
        lst.pop()

print(lst.sum())