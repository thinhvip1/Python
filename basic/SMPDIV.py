def solve(n, x, y):
    for i in range(2,n,1):
        if(i % x == 0 and i % y != 0):
            print(i, end=" ")
    print("")

t = int(input())
for i in range(t):
    n,x,y = map(int, input().split())
    solve(n,x,y)

