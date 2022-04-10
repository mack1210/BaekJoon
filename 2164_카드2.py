class Que:
    def __init__(self):
        self.q = {}
        self.i_start = 0
        self.i_total = 0
    
    def push(self, x):
        self.q[self.i_total] = x
        self.i_total += 1
    
    def pop(self):
        if self.i_start  != self.i_total:
            pop_val = self.q[self.i_start]
            self.i_start += 1
            return pop_val
        
    def length(self):
        return self.i_total - self.i_start
        
    # def show(self):
    #     print(self.i_start, self.i_total)
    #     print(self.q)
        
    def get_last(self):
        return self.q[self.i_start]

q = Que()

N = int(input())

# add all cards in to the que
for i in range(1, N+1):
    q.push(i)

while q.length()-1:
    q.pop()
    q.push(q.pop())

print(q.get_last())
    