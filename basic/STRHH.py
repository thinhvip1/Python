def solve(str):
    for i in range(len(str)//2):
        if(i%2==0):
            print(str[i],end="")

t = int(input())
for i in range(t):
    str = input()
    solve(str)
    print("")