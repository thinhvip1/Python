import math
def sum(num1, num2):
    if(num1 == math.floor(num1) or num2 == math.floor()):
        return int(num1 + num2)
    else:
        return float(num1 + num2)

t = int(input())
for i in range(t):
    num1,num2 = map(float,input().split())
    print(sum(num1,num2))
