# ### deque를 사용하지 않고 풀려고 했으나 실패
# import sys

# class Que:
#     def __init__(self):
#         self.lst = []
#         self.theFront = 0
#         self.theEnd = 0
    
#     def lenth(self):
#         if len(self.lst) == self.theFront and self.theFront != 0:
#             return 0
#         else:
#             return len(self.lst[self.theFront:self.theEnd])
    
#     def push(self, X):
#         self.lst.append(X)
#         self.theEnd = self.lenth() + 1
    
#     def pop(self):
#         if self.lenth():
#             pop_val = self.lst[self.theFront]
#             self.theFront += 1
#             return pop_val
#         else:
#             return -1

#     def size(self):
#         return self.lenth()
    
#     def empty(self):
#         if self.lenth():
#             return 0
#         else:
#             return 1
    
#     def front(self):
#         if self.lenth():
#             return self.lst[self.theFront]
#         else:
#             return -1
    
#     def back(self):
#         if self.lenth():
#             return self.lst[self.theEnd-1]
#         else:
#             return -1
    

# N = int(input())
# q = Que()

# for i in range(N):
#     inputs = sys.stdin.readline().split()
#     order = inputs[0]
    
#     if len(inputs) == 2 and order == 'push':
#         q.push(inputs[1])
#     else:
#         x = getattr(q, order)
#         print(x())



### deque를 사용하여 시간초과 에러 해결
### subclass 개념을 도입하여 시도

# import sys
# from collections import deque

# class Que(deque):
#     def __init__(self):
#         self._queue = super()
#         self.lst = []
        
#         self.i_start = 0
    
#     def push(self, X):
#         self._queue.append(X)
#         self.lst.append(X)
    
#     def popleft(self):
#         if self.size():
#             print(self._queue.popleft())
#             self.i_start += 1
#         else:
#             print(-1)
        
#     def lenth(self):
#         return len(self.lst)

#     def size(self):
#         return len(self.lst[self.i_start:])
    
#     def empty(self):
#         if self.i_start == self.lenth():
#             return 1
#         else:
#             return 0
    
#     def front(self):
#         if self.empty():
#             return -1
#         else:
#             return self.lst[self.i_start]
    
#     def back(self):
#         if self.empty():
#             return -1
#         else:
#             return self.lst[-1]
    

# N = int(input())
# q = Que()

# for i in range(N):
#     inputs = sys.stdin.readline().split()
#     order = inputs[0]
    
#     if len(inputs) == 2 and order == 'push':
#         q.push(inputs[1])
#     elif order == 'pop':
#         q.popleft()
#     else:
#         x = getattr(q, order)
#         print(x())

### 또 실패하여 dictionary를 도입해 풀어보았다.
import sys

class Que():
    def __init__(self):
        self.que = {}
        
        self.i_start = 0
        self.i_total = 0
    
    def push(self, X):
        self.que[self.i_total] = X
        self.i_total += 1
    
    def size(self):
        return self.i_total - self.i_start
    
    def pop(self):
        if self.i_total - self.i_start:
            pop_val = self.que[self.i_start]
            self.i_start += 1
            return pop_val
        else:
            return -1

    def empty(self):
        if self.i_total - self.i_start:
            return 0
        else:
            return 1
    
    def front(self):
        if self.i_total - self.i_start:
            return self.que[self.i_start]
        else:
            return -1
    
    def back(self):
        if self.i_total - self.i_start:
            return self.que[self.i_total-1]
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
