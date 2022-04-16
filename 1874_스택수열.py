'''https://my-coding-notes.tistory.com/81
스택의 push, pop을 이용하여 입력된 수열을 만드는 문제이다.
스택을 만들어 1부터 n까지 push 연산을 하면서
중간에 수열에 해당하는 숫자가 나오면 pop을 해주고 수열의 비교 인덱스를 하나 증가시키면 된다.
스택 연산으로 수열을 만들 수 없는 경우 NO를 출력해야 하는데, 
적절할 때 pop 연산을 수행할 수 없다는 의미이므로
스택에 n 보다 높은 숫자를 push 해야 하는 경우 NO를 출력하면 된다.
이하 정답
'''
import sys
input = sys.stdin.readline
n = int(input())
seq = [int(input()) for i in range(n)]

stack = []
index = 0
num = 1
cal = []
while(index!=n):
    if stack and stack[-1] == seq[index]:
        stack.pop()
        index += 1
        cal.append("-")
    else:
        if num > n:
            print("NO")
            break
        stack.append(num)
        num += 1
        cal.append("+")
else:
    print(*cal)