### deque를 사용하지 않고 풀려고 했으나 실패
import sys

class Que:
    def __init__(self):
        self.lst = []
        self.theFront = 0
        self.theEnd = 0
    
    def lenth(self):
        if len(self.lst) == self.theFront and self.theFront != 0:
            return 0
        else:
            return len(self.lst[self.theFront:self.theEnd])
    
    def push(self, X):
        self.lst.append(X)
        self.theEnd = self.lenth() + 1
    
    def pop(self):
        if self.lenth():
            pop_val = self.lst[self.theFront]
            self.theFront += 1
            return pop_val
        else:
            return -1

    def size(self):
        return self.lenth()
    
    def empty(self):
        if self.lenth():
            return 0
        else:
            return 1
    
    def front(self):
        if self.lenth():
            return self.lst[self.theFront]
        else:
            return -1
    
    def back(self):
        if self.lenth():
            return self.lst[self.theEnd-1]
        else:
            return -1
    

N = int(input())
q = Que()

for i in range(N):
    inputs = sys.stdin.readline().split()
    order = inputs[0]
    
    if len(inputs) == 2 and order == 'push':
        q.push(inputs[1])
    else:
        x = getattr(q, order)
        print(x())



