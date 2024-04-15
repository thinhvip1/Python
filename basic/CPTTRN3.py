def solve(lines, columns):
    for i in range(3*lines+1):
        for j in range(3*columns+1):
            if (i % 3 == 0 or j % 3 == 0):
                print("*",end="")
            else:
                print(".",end="")
        print("")

t = int(input())
for i in range(t):
    lines, columns = map(int, input().split())
    solve(lines, columns)
    print("")