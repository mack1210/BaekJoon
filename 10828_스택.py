import sys

# Stack Class를 정의
class Stack:
    def __init__(self) -> None:
        self.lst = []
    
    def __str__(self):
        print(self.lst)
    
    def push(self, X):
        self.lst.append(X)
    
    def pop(self):
        if len(self.lst):
            self.val = self.lst[-1]
            self.lst = self.lst[:-1]
            return self.val
        else:
            return -1

    def size(self):
        return len(self.lst)
        
    def empty(self):
        if len(self.lst):
            return 0
        else:
            return 1
            
    def top(self):
        if len(self.lst):
            return self.lst[-1]
        else:
            return -1



N = int(input())
lst = Stack()

for _ in range(N):
    # input()은 runtime 에러가 난다
    # 몇 개로 쪼개질지 알 수 없다면 그냥 한 개의 변수로 일단 받는다.
    temp_input = sys.stdin.readline().split()
    
    # 명령어는 input의 첫 번쨰 factor
    order = temp_input[0]
    # 만약 push라면
    if len(temp_input) == 2 and order == 'push':
        value = temp_input[1]
        lst.push(value)
    # 만약 다른 명령이라면
    else: 
        # getattr을 통해 해당 lst의 order 를 받으며 default message로는 Not parsed를 설정한다.
        # 여기서 lst.pop의 출력은 <bound method Stack.pop of <__main__.Stack object at 0x000001C3D9B481C0>> 의 꼴이고
        # lst.pop()의 출력은 정상적이다.
        # temp에 getattr 클라스를 lst.pop꼴로 주고
        temp = getattr(lst, order, "Not parsed")
        # 프린트 할때 괄호를 붙여 마무리한다.
        print(temp())

    

