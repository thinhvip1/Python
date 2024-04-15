import math

def solve(circle1, circle2):
    distance = math.sqrt(pow(circle1[0]-circle2[0],2) + pow(circle1[1]-circle2[1],2))
    if distance < math.fabs(circle1[2] - circle2[2]):
        print("I")
    elif distance == math.fabs(circle1[2] - circle2[2]):
        print("E")
    else:
        print("O")

t = int(input())
for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    circle1 = (x1,y1,r1)
    circle2 = (x2,y2,r2)
    solve(circle1, circle2)
