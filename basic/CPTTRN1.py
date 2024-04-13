def pattern(lines, columns):
    for i in range(lines):
        for j in range(columns):
            if ((i+j) % 2 == 0):
                print("*", end="")
            else:
                print(".",end="")
        print("")

t = int(input())
for i in range(t):
    lines, columns = map(int, input().split())
    pattern(lines, columns)
    print("")