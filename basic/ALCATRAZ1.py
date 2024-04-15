def sum(num):
    sumDigit = 0
    while num != 0:
        sumDigit += num%10
        num //= 10
    return sumDigit

t = int(input())
for i in range(t):
    num = int(input())
    print(sum(num))