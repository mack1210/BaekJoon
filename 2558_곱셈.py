# 로직은 맞은 듯하나 시간초과
# a = 472 # int(input())
# b = 385 # int(input())
# digits = []
# sum = 0

# while b:
#     if b%10:
#         last = b - b//10 * 10
#         b = b//10
#         digits.append(last)

# for i in range(len(digits)):
#     print(digits[i] * a)
#     sum += ((10**i) * digits[i] * a)

# print(sum)

# 이하 정답 코드
a = int(input())
b = input()
n = len(b)

for i in range(n):
    print(a*int(b[n-i-1]))
print(a*int(b))