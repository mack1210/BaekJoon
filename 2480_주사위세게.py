import numbers


numbers  = list(map(int, input().split()))
N = len(numbers)
n = len(set(numbers))
if n == 1:
    print(10000 + 1000 * numbers[0])
elif n == 2:
    a = numbers.pop(0)
    print(numbers)
    if a in numbers:
        print(1000 + 100 * a)
    else:
        b = numbers.pop(0)
        print(numbers)
        print(1000 + 100 * b)
elif n == 3:
    print(max(numbers) * 100)