def sumSquare(a, b):
    sum = 0
    for i in range(a, b+1, 1):
        sum += i*i
    return sum

a, b = map(int, input().split())
print(sumSquare(a,b))