class Stack:
    def __init__(self):
        self.lst = []
    
    def push(self, X):
        self.lst.append(X)
    
    def pop(self):
        self.lst.pop()

while 1:
    lst = Stack()
    
    vsp = input()
    if vsp == '.':
        break
    match = {"}": "{",
            "]": "[",
            ")": "("}
    
    for _ in vsp:
        if _ in match.values() or _ in match.keys():
            
            if len(lst.lst):
                if _ == "}" and match[_] == lst.lst[-1]:
                    lst.pop()
                elif _ == "]" and match[_] == lst.lst[-1]:
                    lst.pop()
                elif _ == ")" and match[_] == lst.lst[-1]:
                    lst.pop()
                else:
                    lst.push(_)
            else:
                lst.push(_)
        else:
            pass
        
    if len(lst.lst):
        print("no")
    else:
        print("yes")